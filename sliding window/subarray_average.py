# Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

# O(N*K) time | O(K) space
def find_averages_of_subarray_naive(K, arr):
    result = []

    for i in range(len(arr) - K + 1):
        _sum = 0.0
        for j in range(i, i + K):
            _sum += arr[j]
        result.append(_sum / K)
    return result


# O(N) time | O(K) space
def find_averages_of_subarray_optimal(K, arr):
    result = []

    window_start = 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K - 1:
            result.append(window_sum / K)
            window_sum -= arr[window_start]
            window_start += 1
    return result


if __name__ == "__main__":
    solution = find_averages_of_subarray_naive(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Naive Solution: ", solution)
    solution = find_averages_of_subarray_optimal(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Optimal Solution: ", solution)
