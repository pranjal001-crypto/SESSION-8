import unittest
from discount import discount


class TestDiscount(unittest.TestCase):

    def test_negative_total(self):
        with self.assertRaises(ValueError):
            discount(-1)

    def test_50_no_discount(self):
        self.assertEqual(discount(50), 0.0)

    def test_51_discount(self):
        self.assertEqual(discount(51), 0.10)

    def test_over_100_discount(self):
        self.assertEqual(discount(150), 0.20)

    def test_vip_discount(self):
        self.assertEqual(discount(100, True), 0.15)

    def test_max_discount(self):
        self.assertEqual(discount(200, True), 0.25)


if __name__ == "__main__":
    unittest.main()
