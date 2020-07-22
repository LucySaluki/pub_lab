import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.drink_1=Drink("beer", 3.00, 1, 10)
        self.drink_2=Drink("red wine", 2.00, 2, 8)
        self.drinks=[self.drink_1, self.drink_2]

        self.pub = Pub("The Prancing Pony", 100.00, self.drinks)
        self.customer_1 = Customer("Callum", 10.00, 24, 6)
        self.customer_2 = Customer("John", 5.00, 16, 0)
        self.customer_3 = Customer("James", 15.00, 30, 3)

    def test_pub_has_name(self):
        name = self.pub.name
        self.assertEqual("The Prancing Pony", name)

    def test_does_add_to_till(self):
        self.pub.add_money(self.drink_1)
        self.assertEqual(103.00, self.pub.till)

    def test_is_of_age_true(self):
        self.assertTrue(self.pub.is_of_age(self.customer_1))

    def test_is_of_age_false(self):
        self.assertFalse(self.pub.is_of_age(self.customer_2))

    def test_if_too_drunk(self):
        self.assertTrue(self.pub.refuse_service(self.customer_1))

    def test_if_not_drunk(self):
        self.assertFalse(self.pub.refuse_service(self.customer_3))

    def test_stock_level(self):
        total = self.pub.stock_value(self.drinks)
        self.assertEqual(46, total)