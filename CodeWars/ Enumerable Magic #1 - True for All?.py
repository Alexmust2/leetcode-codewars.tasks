greater_than_9 = lambda x: x>9
less_than_9 = lambda x: x<9


def _all(seq, fun):       
    for i in seq:
        if fun(i):
            continue
        else:
            return False
    return True


print(_all((1, 2, 3, 4, 5), greater_than_9))