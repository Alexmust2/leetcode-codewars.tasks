def solution(a, b):
    if len(a) > len(b):
        ls = [b,a,b]
    if len(a) < len(b):
        ls = [a,b,a]
    return "".join(ls)



print(solution("45","1"))