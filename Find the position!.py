def position(alphabet):
    a = 'abcdefghijklmnopqrstuvwxyz'
    pos = a.index(alphabet) + 1
    return f"Position of alphabet: {pos}"


print(position("a"))