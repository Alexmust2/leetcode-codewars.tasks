def abbrev_name(name):
    name = name.split()
    first = name[0][0]
    second = name[1][0]
    return first.upper()+"."+second.upper()


print(abbrev_name("Sam Harris"))