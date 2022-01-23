def solution(string):
    string = list(string)
    result = ""
    for _ in range(len(string)):
        result += string.pop()
    return result