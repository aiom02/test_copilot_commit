import unittest

from app.fib import fib


class TestFib(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(fib(0), 0)

    def test_one(self):
        self.assertEqual(fib(1), 1)

    def test_five(self):
        self.assertEqual(fib(5), 5)


if __name__ == "__main__":
    unittest.main()
