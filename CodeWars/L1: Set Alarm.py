def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    return False



print(set_alarm(False, False))