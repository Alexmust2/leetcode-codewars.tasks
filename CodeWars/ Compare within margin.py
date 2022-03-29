def close_compare(a, b, margin=0):
    if abs(a - b) <= margin:
        return 0
    if a < b:
        return -1
    return 1


print(close_compare(8, 5, 15))