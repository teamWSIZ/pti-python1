import unittest


def good_span(lista, span):
    # `lista` -- to jest lista liczb całkowitych
    # `span` to liczba całkowita...
    liczba_max = lista[0]
    for l in lista:
        if l > liczba_max:
            liczba_max = l
    # tutaj liczba_max to największa liczba w liście `lista`
    liczba_min = lista[0]
    for l in lista:
        if l < liczba_min:
            liczba_min = l
    # tutaj liczba_min to najminiejsza liczba w liście `lista`
    if liczba_max - liczba_min <= span:
        return True
    else:
        return False


class TestSum(unittest.TestCase):

    def test_1(self):
        self.assertEqual(good_span([1, 2, 3], span=5), True, '')

    def test_2(self):
        self.assertEqual(good_span([0, 10, 3, 1], span=8), False, '')

    def test_3(self):
        self.assertEqual(good_span([-5, 5], span=10), True, '')

    def test_4(self):
        self.assertEqual(good_span([0, 0, 0], span=1), True, '')

    def test_5(self):
        self.assertEqual(good_span([0, 10, 20, 30], span=25), False, '')


if __name__ == '__main__':
    unittest.main()
