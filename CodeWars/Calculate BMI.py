def bmi(weight, height):
    res = weight / height ** 2
    if res <= 18.5:
        return "Underweight"
    elif res <= 25.0:
        return "Normal"
    elif res <= 30.0:
        return "Overweight"
    else:
        return "Obese"

print(bmi(50, 1.80))