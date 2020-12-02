
def same_parzyste(w):
    for i in w:
        if i%2==1:
            return False
    return True

print(same_parzyste([1,1]))
print(same_parzyste([2,0]))