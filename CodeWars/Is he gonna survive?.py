
def hero(bullets, dragons):
    if bullets < dragons*2:
        return False
    return True


print(hero(10, 5))