def reverse_seq(n):
    lst = []
    for i in range(n+1):
        if i > 0:
            lst.append(i)
    return(lst[::-1])



print(reverse_seq(5))