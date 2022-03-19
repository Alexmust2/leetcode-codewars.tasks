def fake_bin(x):
    string = ''
    for num in x:
        for i in num:
            if int(i) < 5:
                string += '0'
            elif int(i) >= 5:
                string += '1'
    return string



print(fake_bin(["45385593107843568"]))