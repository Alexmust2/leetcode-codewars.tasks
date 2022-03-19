def str_count(strng, letter):
    cnt = 0
    for elem in strng:
        if elem == letter:
            cnt += 1
    return cnt


print(str_count("hello", "l"))