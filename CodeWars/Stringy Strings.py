def stringy(size): 
    ls = []
    for i in range(size+1):
        ls.append(i%2)
        str_ls = [str(x) for x in ls]
    return "".join(str_ls[1:])
        

print(stringy(3))