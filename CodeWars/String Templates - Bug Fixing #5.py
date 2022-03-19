def build_string(*args):
    ls = ", ".join(args[::])
    return f"I like {ls}!"


print(build_string("Cheese","Milk","Chocolate"))