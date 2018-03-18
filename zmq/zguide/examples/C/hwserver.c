//  Hello World server
//  https://github.com/booksbyus/zguide [navigate to examples/c folder]
//  gcc hwclient.c -D_GNU_SOURCE -l"zmq" -o hwclient

/*
    This server has a dual role.
    (1) It listens on a REP socket and loops back messages adding it's signature [RPC]
    (2) It acts as a server for notifications
    
    We use a timerfd to poll() on both the notification socket and our transmission period

*/

#include <zmq.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <assert.h>

#include <sys/timerfd.h>
#include <time.h>
#include <stdlib.h>
#include <stdint.h>        /* Definition of uint64_t */
#include "zmq.h"

#define CHANNEL_ID "gvm"
#define PUB_SUB_PORT 4040

int main (void)
{
    struct itimerspec tout = {0};
    // period
    tout.it_interval.tv_sec = 3;
    tout.it_interval.tv_nsec = 0;
    tout.it_value.tv_sec = 3;
    tout.it_value.tv_nsec = 0;
    
    // create the timer FD
    int tfd = timerfd_create(CLOCK_REALTIME, 0);
    if (tfd == -1)
       printf("timerfd_create error\n");

    // Arm the timer
    if (timerfd_settime(tfd, 0, &tout, NULL) == -1)
       printf("timerfd_settime error\n");
       
    void *context = zmq_ctx_new ();
	void* publisher = zmq_socket(context, ZMQ_PUB);
    int conn = zmq_bind(publisher, "tcp://*:4040");

    //Socket to talk to clients
    void *responder = zmq_socket (context, ZMQ_REP);
    int rc = zmq_bind (responder, "tcp://*:5555");
    assert (rc == 0);       
       
    // Poll on the timer and notifications
        int id = 0;
        while (1) {
        char msg [256];
        zmq_pollitem_t items [] = {
            { 0,   tfd, ZMQ_POLLIN, 0 },
            { responder, 0, ZMQ_POLLIN, 0 }
        };
        zmq_poll (items, 2, -1);
        if (items [0].revents & ZMQ_POLLIN) {
        	uint64_t exp;
        	read(tfd, &exp, sizeof(uint64_t));
			
			uint8_t payload[128];
			sprintf(payload, "%s %d\n", CHANNEL_ID, id++);
			
			int size = zmq_send (publisher, payload, strlen (payload), 0);
			printf("TX[%d]: %s\n",size, payload);
        }
        if (items [1].revents & ZMQ_POLLIN) {
            int size = zmq_recv (responder, msg, 255, 0);
            if (size != -1) {
                //  Process RPC
                msg[size] = '\0';
                printf("RX:%s", msg);
                sprintf(msg + strlen(msg), "%d-gvm\n", id);
                int size = zmq_send (responder, msg, strlen (msg), 0);
            }
        }
    }


    while (1) {
        char buffer [10];
        zmq_recv (responder, buffer, 10, 0);
        printf ("Received Hello\n");
        sleep (1);          //  Do some 'work'
        zmq_send (responder, "World", 5, 0);
    }
    return 0;
}
