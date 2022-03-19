def remove_char(s):
    s = list(s)
    del s[0]
    del s[-1]
    return "".join(s)



print(remove_char('eloquent'))