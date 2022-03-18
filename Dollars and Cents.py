def format_money(amount):
    money = f"{amount:.2f}"
    return f"${money}"


print(format_money(3.1))