
def no_boring_zeros(n):
    if n == 0:
        return 0
    n = str(n)
    return int(n.rstrip("0")) 
        




print (no_boring_zeros(105000))