def greet(name, owner):
    if name == owner:
        return "Hello boss"
    return "Hello guest"


print(greet('Daniel', 'Daniel'))