def create_array(n):
    res=[]
    for i in range(n+1):
        res.append(i)
    return res[1:]


print(create_array(10))