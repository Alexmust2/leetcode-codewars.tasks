lst =  [3, 5, 8, 13]

def each_cons(lst, n):
    x = len(lst)
    for i in range(1, x):
        print([lst[j] for j in range(x) if (i & (1 < j))])



print(each_cons(lst, 2))