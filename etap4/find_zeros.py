import unittest


def find_zeros(tab):
    """Spradzić czy w tablicy jest 0 w jakimkolwiek miejscu"""

    return False


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_zeros([[0, 1], [0, 2]]), True, '')

    def test_2(self):
        self.assertEqual(find_zeros([[0, 1, 2], [0, 1, 2], [0, 1, 3]]), True, '')

    def test_3(self):
        self.assertEqual(find_zeros([[2, 1, 2], [1, 1, 1], [3, 1, 1]]), False, '')

    def test_4(self):
        self.assertEqual(find_zeros([[3], [2], [1]]), False, '')


if __name__ == '__main__':
    unittest.main()
