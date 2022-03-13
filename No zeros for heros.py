def no_boring_zeros(n):
    n = str(n)
    for i in n:
        while i == "0":
            n += n.replace("0", "")
    return n
    



print (no_boring_zeros(960000))