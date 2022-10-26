import unittest
from src.drink import Drink
# from src.pub import Pub
# from src.customer import Customer

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.beer = Drink("beer", 5)
        self.wine = Drink("wine", 6.50)

    def test_drink_name(self):
        self.assertEqual("beer", self.beer.name)

    def test_drink_price(self):
        self.assertEqual(6.50, self.wine.price)