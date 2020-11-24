import unittest


def is_winner(tab, char):
    """Sprawdzić warunek zwycięstwa dla znaku w zmiennech `char` """

    return False


def find_zeros(tab):
    """Podać zwycięzcę gry kółko i krzyżyk: 'x' lub 'o' lub '.' jeśli nikt nie wygrał"""
    if is_winner(tab, 'x'):
        return 'x'
    if is_winner(tab, 'o'):
        return 'o'
    return '.'  # remis


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(find_zeros([['.', '.', '.'], ['.', '.', '.'], ['x', 'x', 'x']]), 'x', '')

    def test_2(self):
        self.assertEqual(find_zeros([['.', 'o', '.'], ['.', 'o', '.'], ['x', 'o', 'x']]), 'o', '')

    def test_3(self):
        self.assertEqual(find_zeros([['x', '.', '.'], ['o', 'x', 'o'], ['x', 'o', 'x']]), 'x', '')

    def test_4(self):
        self.assertEqual(find_zeros([['.', '.', '.'], ['.', '.', '.'], ['x', '.', 'x']]), '.', '')


if __name__ == '__main__':
    unittest.main()

[
    ['.', 'o', '.'],
    ['.', 'o', '.'],
    ['x', 'o', 'x']]
