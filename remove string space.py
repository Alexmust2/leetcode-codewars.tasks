def no_space(x):
    res = []
    for ele in x:
        if ele.strip():
            res.append(ele)
    return "".join(res)
print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))