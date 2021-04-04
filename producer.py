"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread
from time import sleep

class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.products = products
        self.marketplace = marketplace
        self.republish_wait_time = republish_wait_time

        self.id = self.marketplace.register_producer()
        self.name = kwargs['name']
        self.setDaemon(kwargs['daemon'])

    def run(self):
        while 1:
            # traverse through products
            for product in self.products:
                param2 = product[1]
                for traverse in range(param2):
                    param1 = product[0]
                    while not self.marketplace.publish(self.id, param1):
                        # If the list for this producer is full, wait
                        sleep(self.republish_wait_time)
                    # If the product has been published successfully, wait
                    sleep(product[2])
