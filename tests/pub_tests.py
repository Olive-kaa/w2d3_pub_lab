import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("Black Bull", 500)
        self.beer = Drink("beer", 5)
        self.wine = Drink("wine", 6.50)
        self.customer = Customer("Bill", 100, 25)

    def test_pub_has_name(self):
        self.assertEqual("Black Bull", self.pub.name)

    def test_pub_till(self):
        self.assertEqual(500, self.pub.till)

    def test_drink_sold(self):
        self.pub.increase_till(self.beer.price)
        self.assertEqual(505, self.pub.till)

    def test_customer_age(self):
        customer_age_statement = self.pub.check_age(self.customer.age)
        self.assertEqual("What would you like?", customer_age_statement)
