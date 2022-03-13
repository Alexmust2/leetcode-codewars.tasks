def hello(name=""):
    if name == "":
        return "Hello, World!"
    name = name.lower()
    s = name[0]
    s = s.upper()
    name = s + name[1:]
    return f"Hello, {name}!"

print(hello("John"))