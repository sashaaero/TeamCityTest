import unittest
from scripts.foo import *
from utils import get_test_runner


class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 10), 15)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5)

    def test_mul(self):
        self.assertEqual(mul(5, 10), 50)

    def test_div(self):
        self.assertEqual(div(10, 5), 2)

    def test_div_2(self):
        with self.assertRaises(ZeroDivisionError) as context:
            div(10, 0)
        self.assertTrue('You cannot divide by 0' in str(context.exception))

    def test_pow(self):
        self.assertEqual(pow(10, 2), 100)

    def test_mod(self):
        import sys
        if sys.version_info[0] == 2:
            raise ZeroDivisionError
        self.assertEqual(mod(10, 2), 0)


if __name__ == '__main__':
    unittest.main(testRunner=get_test_runner())