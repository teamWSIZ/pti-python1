w = [[1, 2], [3, 4], [5, 6]]
print(w)
print(w[0])  # [1,2]
print(w[1])  # [3,4]

print(len(w))  # 3 -- tyle rzędów
print(len(w[0]))  # 2 -- tyle kolumn (w rzędzie 0)

print(w[0][1])  # =2, element w rzędzie nr 0, w kolumnie nr 1
print(w[2][0])  # =5, element w rzędzie nr 2, kolumnie 0

# iteracja po rzędach

# iteracja po kolumnach


n = len(w)  # liczba rzędów
s1 = 0
for i in range(n):
    s1 += w[i][1]
print(s1)  # =12, = 2 + 4 + 6


