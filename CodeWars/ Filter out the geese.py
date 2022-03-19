geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    for j in geese:
        if j in birds:
            birds.remove(j)
    return birds
    


print(goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"]))