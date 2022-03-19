def find_average(nums):
    if nums == []:
        return 0
    return sum(nums) / len(nums)


print(find_average([1, 3, 4, 5]))