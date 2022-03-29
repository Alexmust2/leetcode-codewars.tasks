def is_vow(inp):
    vowel = {97: "a", 101: "e", 105: "i", 111:"o", 117: "u"}
    ls = []
    for i in inp:
        ls.append(i)
        if i in vowel:
            ls.append(vowel[i])
            ls.remove(i)
    return ls



print(is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106]))