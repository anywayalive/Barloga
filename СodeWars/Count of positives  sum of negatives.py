# Given an array of integers.

# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

# If the input array is empty or null, return an empty array.


def count_positives_sum_negatives(arr):
    if arr == []:
        return arr
    else:
        positive_count = 0
        negative_sum = 0
        for n in arr:
            if n > 0:
                positive_count += 1
            elif n < 0:
                negative_sum += n
        return [positive_count, negative_sum]