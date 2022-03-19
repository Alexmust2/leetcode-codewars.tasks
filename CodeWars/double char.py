def double_char(s):
    string = ""
    for char in s:
        string += char*2
    return string

print(double_char("String"))