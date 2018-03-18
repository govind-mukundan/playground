//  Hello World client
//  https://github.com/booksbyus/zguide [navigate to examples/c folder]
// > gcc hwclient.c -D_GNU_SOURCE -l"zmq" -o hwclient

/*
    This client has a dual role.
    (1) It sends out a message to a server every 5 seconds and gets the response [RPC]
    (2) It waits on notification messages from the server
    
    We use a timerfd to poll() on both the notification socket and our transmission period

*/

#include <string.h>
#include <stdio.h>
#include <unistd.h>

#include <sys/timerfd.h>
#include <time.h>
#include <stdlib.h>
#include <stdint.h>        /* Definition of uint64_t */
#include "zmq.h"


int main (void)
{

    struct itimerspec tout = {0};
    // period
    tout.it_interval.tv_sec = 5;
    tout.it_interval.tv_nsec = 0;
    tout.it_value.tv_sec = 5;
    tout.it_value.tv_nsec = 0;
    
    // create the timer FD
    int tfd = timerfd_create(CLOCK_REALTIME, 0);
    if (tfd == -1)
       printf("timerfd_create error\n");

    // Arm the timer
    if (timerfd_settime(tfd, 0, &tout, NULL) == -1)
       printf("timerfd_settime error\n");
               
    printf ("Connecting to hello world server...\n");
    void *context = zmq_ctx_new ();
    void *requester = zmq_socket (context, ZMQ_REQ);
    zmq_connect (requester, "tcp://localhost:5555");
    
    void* subscriber = zmq_socket(context, ZMQ_SUB);
    int conn = zmq_connect(subscriber, "tcp://localhost:4040");
    conn = zmq_setsockopt(subscriber, ZMQ_SUBSCRIBE, 0, 0);
    
    int size;
    // Poll on the timer and notifications
        while (1) {
        char msg [256];
        zmq_pollitem_t items [] = {
            { 0,   tfd, ZMQ_POLLIN, 0 },
            { subscriber, 0, ZMQ_POLLIN, 0 }
        };
        zmq_poll (items, 2, -1);
        if (items [0].revents & ZMQ_POLLIN) {
        	uint64_t exp;
        	read(tfd, &exp, sizeof(uint64_t));
        	
        	/* An RPC is expected to work as so from the client perspective - send() + recv() [timeout tbd] */
        	sprintf(msg, "%s", "Hello from Client ");
        	int size = zmq_send (requester, msg, strlen (msg), 0);
			printf("Sending %s\n", msg);
		    size = zmq_recv (requester, msg, 255, 0);
			if (size != -1) {
            	msg[size] = '\0';
				printf("RX %s\n", msg);
            }
        }
        if (items [1].revents & ZMQ_POLLIN) {
            size = zmq_recv (subscriber, msg, 255, 0);
            if (size != -1) {
            	msg[size] = '\0';
				printf("%s\n", msg);
            }
        }
    }
    
    
    int i;
    for(i = 0; i < 10; i++) {
        zmq_msg_t reply;
        zmq_msg_init(&reply);
        zmq_msg_recv(&reply, subscriber, 0);
        int length = zmq_msg_size(&reply);
        char* value = malloc(length);
        memcpy(value, zmq_msg_data(&reply), length);
        zmq_msg_close(&reply);
        printf("%s\n", value);
        free(value);
    }
    zmq_close(subscriber);
    zmq_ctx_destroy(context);

    int request_nbr;
    for (request_nbr = 0; request_nbr != 10; request_nbr++) {
        char buffer [10];
        printf ("Sending Hello %d...\n", request_nbr);
        zmq_send (requester, "Hello", 5, 0);
        zmq_recv (requester, buffer, 10, 0);
        printf ("Received World %d\n", request_nbr);
    }
    zmq_close (requester);
    zmq_ctx_destroy (context);
    return 0;
}
