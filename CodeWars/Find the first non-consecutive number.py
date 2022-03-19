def first_non_consecutive(arr):
    for i, j in enumerate(arr,arr[0]):
            if i != j: 
                return j

    



print(first_non_consecutive([1,2,3,4,6,7,8]))