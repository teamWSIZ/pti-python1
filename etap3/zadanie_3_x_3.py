import unittest


def three(lista):
    cnt = 0
    for c in lista:
        if c == 3:
            cnt += 1
    return cnt >= 3


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(three([1, 2, 3]), False, '')

    def test_2(self):
        self.assertEqual(three([3, 3, 3]), True, '')

    def test_3(self):
        self.assertEqual(three([2, 2, 3, 3, 2, 3]), True, '')

    def test_4(self):
        self.assertEqual(three([0]), False, '')


if __name__ == '__main__':
    unittest.main()
