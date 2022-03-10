def expression_matter(a, b, c):
    ls = []
    plus = (a + b) * c
    mult = a * b * c
    plus_1 = a + b * c 
    else_plus = a * (b + c)
    plus_2 = a + b + c
    ls.append(plus), ls.append(mult), ls.append(plus_1), ls.append(else_plus), ls.append(plus_2)
    return max(ls)
    



print(expression_matter(1, 2, 3))