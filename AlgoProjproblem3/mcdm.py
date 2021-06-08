def min_normalize(arr):
    minValue = min(arr)
    for i in range(len(arr)):
        arr[i] = round(minValue / arr[i], 2)
    return arr


def max_normalize(arr):
    maxValue = max(arr)
    for i in range(len(arr)):
        arr[i] = round(arr[i] / maxValue, 2)


def mcdm_weighted_sum(distance_arr, distance_weightage, semantic_arr, semantic_weightage):
    sum_arr = []
    for i in range(len(distance_arr)):
        value = (distance_arr[i] * distance_weightage) + (semantic_arr[i] * semantic_weightage)
        sum_arr.append(round(value, 2))
    return sum_arr


# to print conclusion of most recommended courier company at dash
def best_courier(mcdm_dict):
    recommended = max(mcdm_dict, key=mcdm_dict.get)
    return recommended + " is the most recommended based on distance and sentiment analysis."
