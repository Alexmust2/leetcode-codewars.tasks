def flip(d, a):
    if d == "L":
        a  = sorted(a, reverse=True)
        return a
    return sorted(a, reverse=False)


print(flip("R", [3, 2, 1, 2]))