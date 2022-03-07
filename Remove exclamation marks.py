def remove_exclamation_marks(s):
    s = list(s)
    while "!" in s:
        s.remove("!")
    return "".join(s)
    



print (remove_exclamation_marks("Hello World!"))