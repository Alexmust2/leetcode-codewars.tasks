def weather_info (temp):
    celsius = (temp - 32) * (5/9)
    if celsius > 0:
        return f"{celsius} is above freezing temperature"
    return f"{celsius} is freezing temperature"

    



print(weather_info(50))