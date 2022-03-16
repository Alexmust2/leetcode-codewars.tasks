def find_multiples(integer, limit):
    ls = [integer]
    s = integer
    for i in range(integer+1):
        s += integer
        ls.append(integer)
    return ls[:-1]


print(find_multiples(5,25))