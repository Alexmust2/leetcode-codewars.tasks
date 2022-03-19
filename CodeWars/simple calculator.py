def calculator(x,y,op):
    operators = ["+", "-", "*", "/"]
    if str(x).isdigit() and str(y).isdigit() and op in operators: 
        if op == "+":
            return x + y
        if op == "-":
            return x - y
        if op == "*":
            return x * y
        if op == "/":
            return x / y
    return "unknown value"

print(calculator(6, 2, "-"))
