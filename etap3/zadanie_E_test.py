import unittest


def not_decreasing_anymore(list):
    return 0


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(not_decreasing_anymore([9, 8, 6, 1, 2]), 4, '')

    def test_2(self):
        self.assertEqual(not_decreasing_anymore([2, 3]), 1, '')

    def test_3(self):
        self.assertEqual(not_decreasing_anymore([9, 8, 7, 7]), 3, '')

    def test_4(self):
        self.assertEqual(not_decreasing_anymore([9, 8, 7, 6]), 0, '')

    def test_5(self):
        self.assertEqual(not_decreasing_anymore([9, 8]), 0, '')


if __name__ == '__main__':
    unittest.main()
