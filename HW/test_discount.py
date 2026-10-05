import unittest
from discount import discount


class TestDiscount(unittest.TestCase):

    def test_no_discount(self):
        self.assertEqual(discount(500), 0)

    def test_1000_boundary(self):
        self.assertEqual(discount(1000), 10)

    def test_5000_boundary(self):
        self.assertEqual(discount(5000), 20)

    def test_vip(self):
        self.assertEqual(discount(1000, True), 15)

    def test_max_discount(self):
        self.assertEqual(discount(5000, True), 25)


if __name__ == "__main__":
    unittest.main()
