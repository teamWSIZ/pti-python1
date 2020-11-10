import unittest


def wherelast(lista):
    last = -1
    for i in range(len(lista)):
        if lista[i] == 3:
            last = i

    return last


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(wherelast([1, 2, 3]), 2, '')

    def test_2(self):
        self.assertEqual(wherelast([3, 3, 3]), 2, '')

    def test_3(self):
        self.assertEqual(wherelast([2, 2, 3, 3, 2, 3]), 5, '')

    def test_4(self):
        self.assertEqual(wherelast([3]), 0, '')


if __name__ == '__main__':
    unittest.main()
