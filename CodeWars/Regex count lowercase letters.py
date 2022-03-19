def lowercase_count(strng):
    j = 0
    for i in strng:
        if i.islower():
            j += 1
    return j

print(lowercase_count("abc"))