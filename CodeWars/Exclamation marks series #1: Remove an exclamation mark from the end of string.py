def remove(s):
    if s == "":
        return s
    if s[-1] != "!":
        return s
    return s[:-1]

print(remove("!Hi"))