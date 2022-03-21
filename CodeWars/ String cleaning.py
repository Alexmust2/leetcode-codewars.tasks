def string_clean(s):
    empty_list = []
    for i in s:
        if not i.isdigit():
            empty_list.append(i)
    return "".join(empty_list)
print(string_clean("123456789"))