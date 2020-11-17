w = [1, 2, 3, 1]  # lista/tablica

print(w)
print(w[0])
print(w[-1])
print(w[2])
print(len(w))  # liczba elementów w liście

# ------------- listy 2d ... ... lub czasem mówimy "tablice 2d"

t = [[0, 1],
     [1, 2],
     [3, 4]]
print(t)
print(t[0])  # rząd nr 0, [0, 1]
print(len(t))  # podaje liczbę rzędów

print(len(t[0]))  # poda ile elementów w rzędzie 0... czyli de facto liczbę kolumn w tablicy...

print(t[0][1])  # = 1
print(t[2][0])  # = 3


# ------------
boad = [['.', 'p', 'p', 'q'], ['k', 'b', '.', '.']]
# print(boad)



# przejście przez tabilcę
for r in range(len(t)):
    for c in range(len(t[0])):
        print(f'element w rzędzie {r} i kolumnie {c} to: {t[r][c]}')