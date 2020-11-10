import unittest


def no7(lista):
    return True


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(no7([1, 2, 3, 4]), True, '')

    def test_2(self):
        self.assertEqual(no7([1, 1, 0]), True, '')

    def test_3(self):
        self.assertEqual(no7([7, 1, 1]), False, '')

    def test_4(self):
        self.assertEqual(no7([7]), False, '')


if __name__ == '__main__':
    unittest.main()
