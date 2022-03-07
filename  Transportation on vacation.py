def rental_car_cost(d):
    if d >= 7:
        return d * 40 - 50
    if d > 3:
        return d * 40 - 20
    return d * 40

print(rental_car_cost(7))