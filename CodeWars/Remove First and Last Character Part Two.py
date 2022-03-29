def array(string):
    string = string.split(",")
    if len(string) < 3:
        return None
    return " ".join(string[1:-1])


print(array("1,2,3,4"))