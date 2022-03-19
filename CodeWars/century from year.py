import re


def century(year):
    if year >= 1000 and year % 100 == 0:
        return year // 100
    if year >= 1000:
        return year // 100 + 1
    else:
        return year // 100 + 1
 

print(century(1705))