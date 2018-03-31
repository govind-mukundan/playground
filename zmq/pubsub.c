

#include <stdint.h>
#include <stddef.h>
#include <unistd.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h> // memcpy
#include <stdlib.h> // stdlib
#include <assert.h>

#include <zmq.h>
#include <gio/gio.h>

/*

This is an illustration of a PUB --> XSUB ---> XPUB ---> SUB network

NOTE
Be very careful when specifying the address to bind() vs connect() when using TCP
bind() does NOT understand localhost (or any DNS name), instead you can use 
(1) interface:port [eg: eth0:5555]
(2) IP:port
(3) *:port [implies all available interfaces]

https://stackoverflow.com/questions/6024003/why-doesnt-zeromq-work-on-localhost/8958414#8958414

// depends on glib and zmq
gcc pubsub.c -D_GNU_SOURCE -l"zmq" -l"glib-2.0" -o pubsub -I/usr/include/glib-2.0 -I/usr/lib/x86_64-linux-gnu/glib-2.0/include

*/

#define STR_HELPER(x) #x
#define STR(x) STR_HELPER(x)

#define RPC_PORT					8080
#define PLUGIN_NOTIFICATIONS_PORT	8081

#define PLUGIN_SOCK_FMT			"ipc://@/tmp/panl/plugin/%s"
#define BACNET_SOCK				"ipc://@/tmp/panl/plugin/bacnet"
#define PRIMARY_PUB_SOCK		"ipc://@/tmp/panl/primary/pub"


#define RPC_SOCK_TYPE_SVR		ZMQ_REP
#define NOTIF_SOCK_TYPE_SVR		ZMQ_PUB
#define RPC_SOCK_ADDR_SVR		"tcp://*:" STR(RPC_PORT)
//#define RPC_SOCK_ADDR_SVR		"ipc://@/tmp/panl/plugin/bacnet"
#define	NOTIF_SOCK_ADDR_SVR	 	"tcp://*:" STR(PLUGIN_NOTIFICATIONS_PORT)



#define RPC_SOCK_TYPE_CLIENT		ZMQ_REQ
#define NOTIF_SOCK_TYPE_CLIENT		ZMQ_SUB
#define RPC_SOCK_ADDR_CLIENT		"tcp://localhost:" STR(RPC_PORT)
#define	NOTIF_SOCK_ADDR_CLIENT	 	"tcp://localhost:" STR(PLUGIN_NOTIFICATIONS_PORT)


void* g_router_context;

void pub_sub_router(void)
{
	
	void* context = zmq_ctx_new ();
		
	printf("Frontend BINDING to %s\n", NOTIF_SOCK_ADDR_SVR);
    void *frontend = zmq_socket (context, ZMQ_XSUB );
    int rc = zmq_bind(frontend, NOTIF_SOCK_ADDR_SVR); // Publisher is going to connect here
    assert (rc == 0);

    printf("Backend BINDING to %s\n", PRIMARY_PUB_SOCK);
    void *backend = zmq_socket (context, ZMQ_XPUB); // Plugins are going to connect here
    rc = zmq_bind (backend, PRIMARY_PUB_SOCK);
    assert (rc == 0);
    
    zmq_proxy (frontend, backend, NULL);
}


void publish(void)
{

	int count = 0;
	printf("Publisher connecting to %s\n", NOTIF_SOCK_ADDR_CLIENT);
	void* publisher = zmq_socket(g_router_context, ZMQ_PUB);
	int conn = zmq_connect(publisher, NOTIF_SOCK_ADDR_CLIENT);
	char payload[255];

//  zmq_pollitem_t pollitems [] = { { publisher, 0, ZMQ_POLLIN, 0 } };
//	zmq_poll (pollitems, 1, 1);

	while(1){
		sprintf(payload, "[%d] This is a broadcast message to all ye liseners", ++count);
		int size = zmq_send (publisher, payload, strlen (payload), 0);
		printf("Pub %d\n", size);
		sleep(5);
	}
}


void subscribe(void)
{
	printf("Starting subscriber.. %s\n", PRIMARY_PUB_SOCK);
	void* subscriber = zmq_socket(g_router_context, ZMQ_SUB);
	int conn = zmq_connect(subscriber, PRIMARY_PUB_SOCK);
	conn = zmq_setsockopt(subscriber, ZMQ_SUBSCRIBE, 0, 0);
	char msg [256];
	
//    zmq_pollitem_t pollitems [] = { { subscriber, 0, ZMQ_POLLIN, 0 } };
//	zmq_poll (pollitems, 1, 1);

	while(1){
		int size = zmq_recv (subscriber, msg, 255, 0);
      	printf("Sub %s\n", msg);
	}
}

int main(int argc, char* argv[])
{

	g_router_context = zmq_ctx_new ();
/* NOTE how the first message is lost
https://github.com/zeromq/libzmq/issues/2267
*/

GThread* router = g_thread_new("router", pub_sub_router, NULL);
GThread* pub = g_thread_new("publish", publish, NULL);
sleep(3);
GThread* sub = g_thread_new("subscribe", subscribe, NULL);


pause();

return 0;

}
