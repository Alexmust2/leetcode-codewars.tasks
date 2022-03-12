def generate_range(min, max, step): 
    ls = []
    for i in range(min, max+1, step):
        ls.append(i)
    return ls



print(generate_range(1, 10, 1))