def next_id(arr):
    ls = list(range(1  - min(arr), max(arr)+1))
    second_ls = []
    arr.sort()
    for i in ls:
        if i not in arr:
            second_ls.append(i)
        if arr == ls:
            return arr[-1]+1
    return min(second_ls)
print(next_id([9,8,0,1,7,6]))