def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    return "green"
    


print(update_light("green"))