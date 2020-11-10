import unittest


def suma(a,b):
  return a+b


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(suma(1,2), 3, '')

    def test_2(self):
        self.assertEqual(suma(2,2), 4, '')

    def test_3(self):
        self.assertEqual(suma(1,-2), -1, '')

    def test_4(self):
        self.assertEqual(suma(10**10,10**10), 2*10**10, '')



if __name__ == '__main__':
    unittest.main()