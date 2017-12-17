/* A simple LKM */

#include <linux/module.h> // Location -- /usr/src/linux-headers-4.10.0-19/include/linux/

int init_module()
{
        printk(KERN_ALERT "LKM init\n");

        return 0;
}

void cleanup_module()
{
        printk(KERN_ALERT "LKM stopped\n");
}
