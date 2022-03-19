def warn_the_sheep(queue):
    if queue[-1] == "wolf":
        return 'Pls go away and stop eating my sheep'
    s = queue[::-1].index("wolf")
    return f"Oi! Sheep number {s}! You are about to be eaten by a wolf!"


print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))