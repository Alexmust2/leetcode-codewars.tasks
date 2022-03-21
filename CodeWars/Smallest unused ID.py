def next_id(arr):
    if arr == []:
        return 0
    arr.sort()
    arr_list = list(range(0, max(arr)+2))
    empty_list = []
    for i in arr_list:
        if i not in arr:
            empty_list.append(i)
    return min(empty_list)

print(next_id([9,8,0,1,7,6]))