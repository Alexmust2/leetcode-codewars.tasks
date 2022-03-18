def distinct(seq):
    ls = []
    for i in seq:
        if i not in ls:
            ls.append(i)
    return ls



print(distinct([1, 1, 1, 1, 2, 1, 1, 2]))
