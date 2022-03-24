def animals(heads, legs):
    if heads == 0 and legs == 0:
        return (0, 0)
    if heads <= 0 or legs <= 0:
        return "No solutions"
    chickens = heads * 2
    superfluous_legs = legs - chickens 
    if superfluous_legs == 1:
        return "No solutions"
    cow_count = superfluous_legs // 2
    chickens_count = heads - cow_count
    if heads % 2 != 0 and legs % 2 != 0:
        return  "No solutions"
    if cow_count < 0 or chickens_count < 0:
        return  "No solutions"
    return (chickens_count, cow_count)
    
print(animals(54, 956))