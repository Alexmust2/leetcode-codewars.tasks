def add_length(str_):
    str_ = str_.split(" ")
    ls = []
    for i in str_:
        res = len(i)
        ls.append(f"{i} {res}")
    return ls


print(add_length("apple ban"))