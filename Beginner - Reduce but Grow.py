def grow(arr):
    multiply = 1 
    for elem in arr:
        multiply = elem * multiply
    return multiply    
    



print(grow([4,1,1,1,4]))