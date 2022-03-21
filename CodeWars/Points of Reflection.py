def symmetric_point(p, q):
    return [2 * q[0] - p[0], 2 * q[1] - p[1]]


print(symmetric_point([10, -10], [-10, 10]))