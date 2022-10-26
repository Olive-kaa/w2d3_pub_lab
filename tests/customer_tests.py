import unittest
from src.drink import Drink
# from src.pub import Pub
from src.customer import Customer


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Bill", 100, 25)
        self.beer = Drink("beer", 5)
        self.wine = Drink("wine", 6.50)

    def test_customer_name(self):
        self.assertEqual("Bill", self.customer.name)

    def test_customer_wallet(self):
        self.assertEqual(100, self.customer.wallet)

    def test_drink_bought(self):
        self.customer.buy_drink(self.beer.price)
        self.assertEqual(95, self.customer.wallet)