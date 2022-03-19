def enough(cap, on, wait):
    s = on + wait - cap
    if s < 0:
        return 0
    return s


print(enough(20, 5, 5))