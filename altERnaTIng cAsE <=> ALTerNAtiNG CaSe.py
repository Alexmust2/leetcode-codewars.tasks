
def to_alternating_case(string):
    s = ""
    for i in string:
        if i.isupper():
            s += i.lower()
        elif i.islower():
            s += i.upper()
        else:
            s += i
    return s
            

print(to_alternating_case("hello world"))