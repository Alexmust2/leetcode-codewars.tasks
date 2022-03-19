def remove(s):
    s = list(s)
    for i in s[::-1]:
        if i == "!":
            s.remove("!")
    return "".join(s) + "!"


print(remove("Hi!!!"))