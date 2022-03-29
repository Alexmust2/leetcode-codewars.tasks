def kata_13_december(lst):
    ls = []
    for i in lst: 
        if i%2!=0: 
            ls.append(i)
    return ls

print(kata_13_december([1, 2, 2, 2, 4, 3, 4]))