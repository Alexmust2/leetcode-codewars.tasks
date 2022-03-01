def find_average(numbers):
    count = 0
    int = 0
    if numbers == []:
        return 0
    for elem in numbers:
        count += elem
        int += 1
        result = count / int
    return result

print(find_average([1, 2, 3]))