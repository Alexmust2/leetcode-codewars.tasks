def get_drink_by_profession(param):
    arr = {
    "jabroni": "Patron Tequila",
    "school counselor":"Anything with Alcohol",
    "programmer":"Hipster Craft Beer",
    "bike gang member": "Moonshine",
    "politician": "Your tax dollars",
    "rapper": "Cristal",
    }
    if param.lower() in arr:
        return arr[param.lower()]
    return "Beer"

print(get_drink_by_profession("jabrOni"))