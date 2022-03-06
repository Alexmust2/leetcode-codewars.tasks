def better_than_average(class_points, your_points):
    if sum(class_points) // len(class_points) < your_points:
        return True
    return False
    



print(better_than_average([5,7], 5))