def find_multiples(integer, limit):
    ls = []
    rang = limit // integer 
    s = integer
    for i in range(rang+1):
        ls.append(s)
        s += integer
    return ls[:-1]


print(find_multiples(5,25))