import unittest


def last(lista):
  return lista[-1]


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(last([1,2,3]),3,'')
    def test_2(self):
        self.assertEqual(last([1]),1,'')
    def test_3(self):
        self.assertEqual(last([2,2,1]),1,'')
    def test_4(self):
        self.assertEqual(last([0,0,-10]),-10,'')



if __name__ == '__main__':
    unittest.main()