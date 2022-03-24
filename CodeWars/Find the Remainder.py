def remainder(a,b):
    if a == 0 and b < 0 or a < 0 and b == 0:
        return 0
    if a == 0 or b == 0:
        return None
    if a >= b:
        return a % b
    if b > a:
        return b % a

print(remainder(17, 5))