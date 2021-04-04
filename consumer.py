"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Thread, currentThread
from time import sleep

class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        Thread.__init__(self, **kwargs)
        self.carts = carts
        self.marketplace = marketplace
        self.retry_wait_time = retry_wait_time
        self.name = kwargs['name']

    def run(self):
        # traverse through carts
        for cart in self.carts:
            # for each cart, calculate cart_id
            cart_id = self.marketplace.new_cart()
            for model in cart:
                for traverse in range(model['quantity']):
                    # case for 'add' operation
                    if model['type'] == 'add':
                        while not self.marketplace.add_to_cart(cart_id, model['product']):
                            sleep(self.retry_wait_time)
                    # case for 'remove' operation
                    if model['type'] == 'remove':
                        self.marketplace.remove_from_cart(cart_id, model['product'])
            place = self.marketplace.place_order(cart_id)

            # print for every cartn
            for product in place:
                print("{} bought {}".format(currentThread().getName(), product))



