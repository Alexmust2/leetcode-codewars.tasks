def uni_total(s):
    if s == "":
        return 0
    i = 0
    for j in s:
        i+=ord(j)
    return i

print(uni_total("aaaa"))