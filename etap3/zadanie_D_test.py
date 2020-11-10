import unittest


def first_last(list):
    return True


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(first_last([1, 4, 2, 23, 1]), True, '')

    def test_2(self):
        self.assertEqual(first_last([0, 4]), False, '')

    def test_3(self):
        self.assertEqual(first_last([1]), True, '')

    def test_4(self):
        self.assertEqual(first_last([1, 1, 1, 1, 1, 1, 1, 1, 0]), False, '')


if __name__ == '__main__':
    unittest.main()
