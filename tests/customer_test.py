import unittest
from src.customer import Customer
from src.drink import Drink
from src.food import Food

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Callum", 10.00, 24, 0)
        self.drink = Drink("Beer", 3.00, 1,10)
        self.food = Food("Chips", 2.00, 1)

    def test_can_customer_buy_drink(self):
        self.customer.buy_drink(self.drink)
        self.assertEqual(7.00, self.customer.wallet)

    def test_drunk_level(self):
        self.customer.increase_drunk_level(self.drink)
        self.assertEqual(1, self.customer.drunk_level)

    def test_reduce_drunk_level(self):
        self.customer.increase_drunk_level(self.drink)
        self.customer.reduce_drunk_level(self.food)
        self.assertEqual(0, self.customer.drunk_level)