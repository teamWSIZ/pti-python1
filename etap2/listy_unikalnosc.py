w = [1, 3, 2, 2, 4, 5]  # pierwszy test
# w = [1, 3, 2, 4, 5]   # drugi test

# zadanie sprawdzić czy każda z liczb między 1 i 5 występuje w tej tablicy dokładnie raz

# rozwiązanie:
licznik = [0, 0, 0, 0, 0, 0]  # nowa lista będzie zliczać ile jest których elementów

for i in w:
    licznik[i] += 1  # pojawia się liczba `i` -- zwiększamy licznik dla niej o 1

licznik[0] = 1  # zero nie występuje,ale ustawmy sobie tu 1 dla prostoty algorytmu poniżej

all_good = True

for j in licznik:
    if j != 1:
        all_good = False

if all_good:
    print('Wszystkie liczby występują w liście dokładnie 1 raz')
else:
    print('Niektóre liczby występują w liście mniej lub więcej niż 1 raz')
