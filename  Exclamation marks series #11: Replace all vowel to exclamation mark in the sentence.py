def replace_exclamation(s):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    for ch in s:
        if ch in vowels: 
            print(ch)
            s = s.replace(ch, '!') 
    return s
print(replace_exclamation("!Hi! Hi!"))