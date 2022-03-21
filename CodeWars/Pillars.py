def pillars(num_pill, dist, width):
    if num_pill == 1:
        return 0
    if num_pill == 2:
        return dist * 100
    s = 0
    n = 0
    num_pill = num_pill - 2
    while num_pill != n:
        s += width
        n += 1
    return s + (dist * (num_pill + 1)) * 100

print(pillars(11, 15, 30))

