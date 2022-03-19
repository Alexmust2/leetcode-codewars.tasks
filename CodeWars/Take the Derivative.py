def derive(coefficient, exponent): 
    multy = coefficient * exponent
    l = exponent - 1
    return f"{multy}x^{l}"

print(derive(7, 8))