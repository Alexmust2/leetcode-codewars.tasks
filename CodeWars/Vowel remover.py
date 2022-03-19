def shortcut(s):
    s = list(s)
    while "o" in s:
        s.remove("o")
    while "e" in s:
        s.remove("e") 
    while "a" in s:
        s.remove("a")
    while "i" in s:
        s.remove("i")
    while "u" in s:
        s.remove("u")
    return "".join(s)



print(shortcut('hello'))