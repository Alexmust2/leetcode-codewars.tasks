def square_or_square_root(arr):
    ls = []
    for i in arr:
        if i**0.5 % 1 == 0:
            ls.append(int(i**0.5))
        if i**0.5 % 1 != 0:
            ls.append(i**2)
    return ls


print(square_or_square_root([4, 3, 9, 7, 2, 1 ]))