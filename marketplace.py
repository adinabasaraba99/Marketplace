"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2021
"""

from threading import Lock


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """

    def __init__(self, queue_size_per_producer):
        """
        Constructor
        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """
        self.queue_size_per_prod = queue_size_per_producer
        self.stock = {}  # for each producer, the products
        self.products = []   # a list for all the products
        self.carts = []
        self.prod_id = -1
        self.cart_id = -1
        self.lock_register = Lock()  # lock for register_producer
        self.lock_publish = Lock()   # lock for publish
        self.lock_new_cart = Lock()  # lock for new_cart

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        self.lock_register.acquire()  # lock for incrementation
        self.prod_id = self.prod_id + 1
        self.stock[self.prod_id] = []
        self.lock_register.release()
        return self.prod_id

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        self.lock_publish.acquire()
        length = len(self.stock[producer_id])
        # If there is still space in the list of this producer
        if length >= self.queue_size_per_prod:
            return False
        # Add the product
        self.stock[producer_id].append(product)
        self.lock_publish.release()
        return True

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        # lock for incrementation
        self.lock_new_cart.acquire()
        # increment with 1
        self.cart_id = self.cart_id + 1
        self.carts.append([])
        self.lock_new_cart.release()
        return self.cart_id

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """

        # add the product
        for key in self.stock.keys():
            if product in self.stock[key]:
                for prod in self.stock[key]:
                    if prod == product:
                        # If the product exists, delete
                        self.stock[key].remove(product)
                        # Add in list pair (product, key)
                        self.products.append((product, key))
                        self.carts[cart_id].append(product)
                        return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """

        for prd in self.carts[cart_id]:
            if prd == product:
                # if the product is found
                self.carts[cart_id].remove(prd)
                break
        for index, tup in enumerate(self.products):
            if product == tup[0]:
                self.stock[tup[1]].append(product)
                self.products.remove(tup)
                break

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        return self.carts[cart_id]
