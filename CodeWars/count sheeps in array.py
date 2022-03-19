from array import array


def count_sheeps(sheep):
    return sheep.count(True)





array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True ];


print(result := count_sheeps(array1))