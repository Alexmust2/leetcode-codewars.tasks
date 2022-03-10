def switch_it_up(number):
    nums = {0:"Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    for elem in nums:
        if elem == number:
            return nums[elem]


print(switch_it_up(1))