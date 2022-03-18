def merge_arrays(arr1, arr2):
    ls = arr1 +arr2
    ls.sort()
    l = []
    for i in ls:
        if i not in l:
            l.append(i)
    return l
    



print(merge_arrays([1,3,5,7,9,11,12], [1,2,3,4,5,10,12]))