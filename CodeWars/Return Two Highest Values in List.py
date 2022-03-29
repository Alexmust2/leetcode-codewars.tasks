def two_highest(arg1):
    if arg1 == []:
        return []
    if len(arg1) <= 2:
        return arg1
    first = 0
    second = 0
    for i in arg1:
        if i > first:
            first = i
    for i in arg1:
        if second < i < first:
            second = i
    if second > first:
        return [second, first]
    if first > second:
        return [first, second]
    

print(two_highest([15,20,12]))