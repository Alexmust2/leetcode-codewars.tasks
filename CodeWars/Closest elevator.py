def elevator(left, right, call):
    l = abs(call-left)
    r = abs(call-right)
    if r <= l:
        return 'right'
    return 'left'


print(elevator(0,1,0))