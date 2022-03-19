def combat(health, damage):
    result = health -damage
    if result < 0:
        return 0
    return  result


print(combat(100,5))