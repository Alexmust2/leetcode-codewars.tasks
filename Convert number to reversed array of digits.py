def digitize(n):
    n_string = str(n)
    n_map = map(int, n_string)
    n_list = list(n_map)
    return n_list[::-1]