def find_difference(a, b):
    nums = 1
    num = 1
    for i in a:
        num = num * i
    for j in b:
        nums = nums * j
    result = num-nums
    if result < 0:
        return result *-1
    return result


print(find_difference([3, 2, 5], [1, 4, 4]))