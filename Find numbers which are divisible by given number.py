def divisible_by(numbers, divisor):
    divisible = []
    for char in numbers:
        if char % divisor == 0:
            divisible.append(char)
    return divisible


print(divisible_by([1, 2, 3, 4, 5, 6], 2))