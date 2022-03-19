def human_years_cat_years_dog_years(human_years):
    years_dog = 0
    years_cat = 0
    first_year = 15
    second_year = 9
    if human_years == 1:
        return [human_years,first_year,first_year]
    if human_years == 2:
        return [human_years,first_year+second_year,first_year+second_year]
    if human_years > 2:
        years = first_year + second_year
        years_dog = 5 * (human_years - 2)
        years_cat = 4 * (human_years - 2)
    return [human_years,years_cat+years,years_dog+years]


print(human_years_cat_years_dog_years(10))