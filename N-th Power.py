def index(array, n):
    if len(array) <= n:
        return -1
    result = array[n] ** n
    return result



print(index([1, 2, 3, 4],2))