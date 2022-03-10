def twice_as_old(dad_years_old, son_years_old):
    age = dad_years_old - son_years_old * 2
    if age < 0:
        age = age * -1
    return age

print(twice_as_old(36,7))