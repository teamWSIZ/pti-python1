import unittest


def largest_row(tab):
    """Znaleźć rząd z najwięszym elementem w tablicy"""

    return []


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(largest_row([[0, 1], [0, 2]]), [0, 2], '')

    def test_2(self):
        self.assertEqual(largest_row([[0, 1, 2], [0, 1, 2], [0, 1, 3]]), [0, 1, 3], '')

    def test_3(self):
        self.assertEqual(largest_row([[2, 1, 2], [1, 1, 1], [3, 1, 1]]), [3, 1, 1], '')

    def test_4(self):
        self.assertEqual(largest_row([[3], [2], [0]]), [3], '')


if __name__ == '__main__':
    unittest.main()
