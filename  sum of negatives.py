def count_positives_sum_negatives(arr):
    positives = [0]
    negatives = [0]
    list = []
    if arr == list:
        return list
    for char in arr:
        if char > 0:
            positives[0] += 1
        else:
            negatives[0] += char
    return positives + negatives

print(count_positives_sum_negatives([]))