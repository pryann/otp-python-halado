import unittest
from util_fns import summarize, subtract, divide


class TestUtilFns(unittest.TestCase):
    def test_summarize(self):
        self.assertEqual(summarize(2, 3), 5)
        self.assertEqual(summarize(-50, 10), -40)
        self.assertEqual(summarize(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(10, 20), -10)
        self.assertEqual(subtract(0, 0), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(9, 3), 3.0)
        # self.assertRaises(ValueError, divide, 5, 0)
        with self.assertRaises(ValueError):
            divide(5, 0)


if __name__ == "__main__":
    unittest.main()
