def multi_table(number):
    n = 1
    ls = []
    for i in range(10):
        while n != 10:
            s = n * number
            ls.append(f"{n} * {number} = {s}\n")
            n += 1
            if n == 10:
                s = n * number
                ls.append(f"{n} * {number} = {s}")
    return "".join(ls)


print(multi_table(5))
