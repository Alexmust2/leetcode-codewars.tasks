


def duty_free(price, discount, holiday_cost):
    saving = price/100*discount
    price = holiday_cost//saving
    return price

print(duty_free(12, 50 , 1000))