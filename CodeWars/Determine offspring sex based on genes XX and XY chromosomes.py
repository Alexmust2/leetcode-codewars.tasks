def chromosome_check(sperm):
    son = "XY"
    if sperm == son:
        return "Congratulations! You\'re going to have a son."
    return 'Congratulations! You\'re going to have a daughter.'



print(chromosome_check("XY"))