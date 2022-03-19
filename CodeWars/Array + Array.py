def array_plus_array(arr1,arr2):
    result = 0
    for elem in arr1:
        result += elem
    for nums in arr2:
        result += nums
    return result
    


print(array_plus_array([-4602, 739, -6416, 9098, -186], [-3412, -5817, -6105, 3221, 9677]))
