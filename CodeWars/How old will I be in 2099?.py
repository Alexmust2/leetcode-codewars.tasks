def calculate_age(year_of_birth, current_year):
    if year_of_birth == current_year:
        return "You were born this very year!"
    if year_of_birth < current_year:
        difference = current_year - year_of_birth
        if difference == 1:
            return f"You are {difference} year old."
        return f"You are {difference} years old." 
    if year_of_birth > current_year:
        difference = year_of_birth - current_year
        if difference == 1:
            return f"You will be born in {difference} year."
        return f"You will be born in {difference} years."

print(calculate_age(2011, 2012))