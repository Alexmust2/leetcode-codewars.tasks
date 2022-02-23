import re


def basic_op(operator, value1, value2):
        if operator == "+":
            return value1 + value2
        if operator == "-":
            return value1 - value2
        if operator == "/":
            return value1 / value2
        if operator == "*":
            return value1 * value2
        


print(basic_op("*", 5, 5))