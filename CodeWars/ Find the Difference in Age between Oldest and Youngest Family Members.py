def difference_in_ages(ages):
    return (min(ages), max(ages), max(ages) - min(ages))

print(difference_in_ages([16, 22, 31, 44, 3, 38, 27, 41, 88]))