import re
from cupshelpers import Printer


def rps(p1, p2):
    s = 'scissors'
    r = 'rock'
    p = 'paper'
    if p1 == p2:
        return "draw"
    elif p1 == r and p2 == s:
        return "Player 1 won"
    elif p2 == r and p1 == s:
        return "Player 2 won"
    elif p1 == p and p2 == r:
        return "Player 1 won"
    elif p2 == p and p1 == r:
        return "Player 2 won"
    elif p1 == s and p2 == p:
        return "Player 1 won"
    elif p2 == s and p1 == p:
        return "Player 2 won"


print(rps('rock', 'scissors'))