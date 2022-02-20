


def positive_sum(arr):
    result = 0
    for char in arr:
        if char > 0:
             result += char
    return result
    


print(positive_sum([1,2,3,4,5]))