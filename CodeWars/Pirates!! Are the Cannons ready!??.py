a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}

def cannons_ready(gunners):
    if all(i == "aye" for i in gunners.values()):
        return "Fire!"
    return 'Shiver me timbers!'

print(cannons_ready(a))


