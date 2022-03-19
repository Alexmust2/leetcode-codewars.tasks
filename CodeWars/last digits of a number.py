def solution(n,d):
    n_list = list(str(n))
    new_list = n_list[-d:]
    if d >= n:
        return [n]
    if d <= 0:
        return []
    return [int(char) for char in new_list]


    
print(solution(34625647867585,10))