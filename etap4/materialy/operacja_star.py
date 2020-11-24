def funkcja(a, b, c, d):
    print(f'a={a} b={b} c={c} d={d}')


funkcja(1, 2, 3, 4)

g = [11, 22, 33, 44]

funkcja(g[0], g[1], g[2], g[3])

funkcja(*g)  # bierze listę liczb, i wstawia kolejne elementy w kolejne pola argumentów funkcji
