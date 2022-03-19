def get_average(marks):
    count = 0
    int = 0
    for elem in marks:
        count += elem
        int += 1
        result = count // int
    return result








print(get_average([2, 2, 2, 2]))