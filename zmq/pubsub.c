

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
The topology is of two publishers that are forwarded to one subscriber using an XPUB/XSUB bridge
 - The subscriber only connects to the XPUB endpoint
 - Publish path: The XSUB interface BINDS to a single /pif/pub endpoint, all publishers connect to this
 - Subscribe ptah: The XPUB binds to <IP><PORT> onto which all interested subscribers connect to
 - The Subscribers must be aware of the TOPICS that are going to be published, if filtering is required

SUBSCRIBER   <------  XPUB+++++XSUB <---- PUB_1
				    <---- PUB_2

NOTE
Be very careful when specifying the address to bind() vs connect() when using *TCP*
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

#define RPC_PORT			8080
#define PLUGIN_NOTIFICATIONS_PORT	8081

#define PLUGIN_SOCK_FMT			"ipc://@/tmp/panl/plugin/%s"
#define BACNET_SOCK			"ipc://@/tmp/panl/plugin/bacnet"
//#define PRIMARY_PUB_SOCK		"ipc://@/tmp/panl/primary/pub"
#define PUBLISH_ENDPOINT		"ipc://@/tmp/panl/pif/pub"


#define RPC_SOCK_TYPE_SVR		ZMQ_REP
#define NOTIF_SOCK_TYPE_SVR		ZMQ_PUB
#define RPC_SOCK_ADDR_SVR		"tcp://*:" STR(RPC_PORT)
//#define RPC_SOCK_ADDR_SVR		"ipc://@/tmp/panl/plugin/bacnet"
#define	NOTIF_SOCK_ADDR_SVR	 	"tcp://*:" STR(PLUGIN_NOTIFICATIONS_PORT)



#define RPC_SOCK_TYPE_CLIENT		ZMQ_REQ
#define NOTIF_SOCK_TYPE_CLIENT		ZMQ_SUB
#define RPC_SOCK_ADDR_CLIENT		"tcp://localhost:" STR(RPC_PORT)
#define	NOTIF_SOCK_ADDR_CLIENT	 	"tcp://localhost:" STR(PLUGIN_NOTIFICATIONS_PORT)


void* g_pub_sub_context;

void pub_sub_router(void)
{
	
    void* context = zmq_ctx_new ();
		
    printf("Frontend BINDING to %s\n", NOTIF_SOCK_ADDR_SVR);
    void *frontend = zmq_socket (context, ZMQ_XPUB );
    int rc = zmq_bind(frontend, NOTIF_SOCK_ADDR_SVR); // Subscribers are going to connect here
    assert (rc == 0);

    printf("Backend BINDING to %s\n", PUBLISH_ENDPOINT);
    void *backend = zmq_socket (context, ZMQ_XSUB); // Publishers are going to connect here
    rc = zmq_bind (backend, PUBLISH_ENDPOINT);
    assert (rc == 0);
    
//  zmq_pollitem_t pollitems [] = { { frontend, 0, ZMQ_POLLIN, 0 },
//  { backend, 0, ZMQ_POLLIN, 0 } };
//	zmq_poll (pollitems, 1, 1);
    
    zmq_proxy (frontend, backend, NULL);
}


void publish_primary(void)
{

	int count = 0;
	printf("Publisher connecting to %s\n", PUBLISH_ENDPOINT);
	void* publisher = zmq_socket(g_pub_sub_context, ZMQ_PUB);
	int conn = zmq_connect(publisher, PUBLISH_ENDPOINT);
	char payload[255];

//  zmq_pollitem_t pollitems [] = { { publisher, 0, ZMQ_POLLIN, 0 } };
//	zmq_poll (pollitems, 1, 1);
	bool init = false;

	while(1){
		sprintf(payload, "[%d] This is a PRIMARY broadcast message to all ye liseners", ++count);
		int size;
		/* To fix the "first message lost issue"
		 * we repeat the first message after a DELAY (required)
		 */
		if(!init){
			size = zmq_send (publisher, payload, strlen (payload), 0);
			printf("[primary] Pub %d\n", size);
			init = true;
			sleep(5);
		}
		size = zmq_send (publisher, payload, strlen (payload), 0);
		printf("[primary] Pub %d\n", size);
		sleep(5);
	}
}

void publish_plugin(void)
{

	int count = 0;
	printf("Publisher connecting to %s\n", PUBLISH_ENDPOINT);
	void* publisher = zmq_socket(g_pub_sub_context, ZMQ_PUB);
	int conn = zmq_connect(publisher, PUBLISH_ENDPOINT);
	char payload[255];

//  zmq_pollitem_t pollitems [] = { { publisher, 0, ZMQ_POLLIN, 0 } };
//	zmq_poll (pollitems, 1, 1);
	bool init = false;

	while(1){
		sprintf(payload, "[%d] This is a PLUGIN broadcast message to all ye liseners", ++count);
		int size;
		/* To fix the "first message lost issue"
		 * we repeat the first message after a DELAY (required)
		 */
		if(!init){
			size = zmq_send (publisher, payload, strlen (payload), 0);
			printf("[plugin] Pub %d\n", size);
			init = true;
			sleep(5);
		}
		size = zmq_send (publisher, payload, strlen (payload), 0);
		printf("[plugin] Pub %d\n", size);
		sleep(5);
	}
}


void subscribe(void)
{
	printf("Starting subscriber.. %s\n", NOTIF_SOCK_ADDR_CLIENT);
	void* subscriber = zmq_socket(g_pub_sub_context, ZMQ_SUB);
	int conn = zmq_connect(subscriber, NOTIF_SOCK_ADDR_CLIENT);
	conn = zmq_setsockopt(subscriber, ZMQ_SUBSCRIBE, 0, 0);
	char msg [256];
	
//  zmq_pollitem_t pollitems [] = { { subscriber, 0, ZMQ_POLLIN, 0 } };
//	zmq_poll (pollitems, 1, 1);

	while(1){
		int size = zmq_recv (subscriber, msg, 255, 0);
      	printf("Sub %s\n", msg);
	}
}

int main(int argc, char* argv[])
{

	g_pub_sub_context = zmq_ctx_new ();
/* NOTE how the first message is lost without the "init" workaround in the publishers
https://github.com/zeromq/libzmq/issues/2267
*/

GThread* router = g_thread_new("router", pub_sub_router, NULL);
GThread* sub = g_thread_new("subscribe", subscribe, NULL);
sleep(3);
GThread* pubp = g_thread_new("publish-plugin", publish_plugin, NULL);
GThread* pubpp = g_thread_new("publish-primary", publish_primary, NULL);
sleep(3);



pause();

return 0;

}
