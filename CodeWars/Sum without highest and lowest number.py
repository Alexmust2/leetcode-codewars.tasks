def sum_array(arr):
    if arr is None or len(arr) <= 2:
        return 0
    return sum(arr) - min(arr) - max(arr)


print(sum_array([6,2,1,8,10]))