def swap_values(args):
    args[0], args[1] = args[1], args[0]
    return args
print(swap_values([1, 2]))