def correct(s):
    if "0" in s:
        s = s.replace("0", "O")
    if "5" in s:
        s= s.replace("5", "S")
    if "1" in s:
        s = s.replace("1", "I")
    return s

print(correct("L0ND0N"))