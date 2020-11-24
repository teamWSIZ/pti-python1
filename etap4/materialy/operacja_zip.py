w = [2, 3, 4, 5]
n = ['alice', 'bob', 'cecile', 'derek']

# for g in zip(w, n):
#     print(g)

a = [0, 1, 2]
b = [0, 1, 2]
c = [0, 1, 3]

for z in zip(a, b, c):
    print(z)

tab = [[0, 1, 2], [5, 5, 5], [7, 7, 8]]

print(*tab)
print(tab[0], tab[1], tab[2])

# for z in zip(tab):
#     print(z)
# #
