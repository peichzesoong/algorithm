def min_normalize(arr):
    minValue = min(arr)
    return [round(minValue / i, 2) for i in arr]

def max_normalize(arr):
    maxValue = max(arr)
    return [round(maxValue / i, 2) for i in arr]

def mcdm_weighted_sum(distance_arr, distance_weightage, semantic_arr, semantic_weightage):
    sum_arr = []
    for i in range(len(distance_arr)):
        value = (distance_arr[i] * distance_weightage) + (semantic_arr[i] * semantic_weightage)
        sum_arr.append(round(value, 2))
    return sum_arr

def best_courier(mcdm_dict):
    recommended = max(mcdm_dict, key=mcdm_dict.get)
    return recommended + " is the most recommended based on distance and sentiment analysis."
