def quarter_of(month):
    first =[1, 2, 3]
    second =[4, 5, 6]
    third =[7, 8, 9]
    if month in first:
        return 1
    if month in second:
        return 2
    if month in third:
        return 3
    return 4


print(quarter_of(3))