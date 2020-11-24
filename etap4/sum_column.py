import unittest


def sum_column(tab):
    """Policzyć sumy każdej z kolumn (zwrócić listę)"""
    ncolumns = len(tab[0])
    result = [0] * ncolumns  # zrobi [0,0,0...] (tyle zer ile kolumn)

    for row in tab:
        for i in range(ncolumns):
            result[i] += row[i]
    return result


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(sum_column([[0, 1], [0, 2]]), [0, 3], '')

    def test_2(self):
        self.assertEqual(sum_column([[0, 1, 2], [0, 1, 2], [0, 1, 3]]), [0, 3, 7], '')

    def test_3(self):
        self.assertEqual(sum_column([[2, 1, 2], [1, 1, 1], [3, 1, 1]]), [6, 3, 4], '')

    def test_4(self):
        self.assertEqual(sum_column([[3], [2], [0]]), [5], '')


if __name__ == '__main__':
    unittest.main()
