def pipe_fix(nums):
    a = nums[-1]
    b = nums[0]
    ls = []
    for i in range(b-1,a+1):
        ls.append(i)
    return ls[1:]


print(pipe_fix([1, 2, 3, 12]))