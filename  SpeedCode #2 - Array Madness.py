def array_madness(a,b):
    res_a = 0
    res_b = 0
    for i in a:
        res_a += i ** 2
    for j in b:
        res_b += j ** 3
    return res_a > res_b



print(array_madness([258], [14, 8, 7, 23, 28, 24, 21, 22]))