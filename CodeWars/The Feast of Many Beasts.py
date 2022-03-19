def feast(beast, dish):
    if beast[0] == dish[0] and dish[-1] == beast[-1]:
        return True
    return False


print(feast(("great blue heron"), ("garlic naan")))