
def triple_trouble(one, two, three):
    n = len(one)
    b = 0
    res = ""
    while n != b:
        n -= 1
        res += one[n-n-1] + two[n-n-1] + three[n-n-1]
    return res[::]

print(triple_trouble("Bm","aa","tn"))