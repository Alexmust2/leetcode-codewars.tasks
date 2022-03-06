def bonus_time(salary, bonus):
    if bonus == 1:
        return "$"+str(salary * 10)
    return "$"+str(salary)

print(bonus_time(10000, True))