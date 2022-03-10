

def how_much_i_love_you(nb_petals):
    words = {
    1:"I love you",
    2:"a little",
    3:"a lot",
    4:"passionately",
    5:"madly",
    6:"not at all"
    }
    if nb_petals not in words:
        nb_petals = nb_petals % len(words)
        if nb_petals == 0:
            nb_petals += 6
            return words[nb_petals]
    if nb_petals in words:
        return words[nb_petals]

    
        


print(how_much_i_love_you(252))