w = [2, 5, 2, 1, 2, 3]


def equal(w):
    e = w[0]
    for i in w:
        if i != e:
            return False
    return True


print(equal(w))
print(equal([1, 1, 1]))
