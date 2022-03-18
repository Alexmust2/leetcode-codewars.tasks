def name_shuffler(str_):
    name = str_.split(' ')
    return " ".join(name[::-1])


print (name_shuffler('john McClane'))