# Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

# Input: [2, 1, 5, 1, 3, 2], k=3
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].

# O(N*K) time | O(K) space
def max_sum_subarray_k_naive(K, arr):
    max_sum = 0

    for i in range(len(arr) - K + 1):
        window_sum = 0
        for j in range(i, i + K):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)
    return max_sum


# O(N) time | O(1) space
def max_sum_subarray_k_optimal(K, arr):
    window_start = 0
    window_sum = 0
    max_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        if window_end >= K - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= arr[window_start]
            window_start += 1
    return max_sum


if __name__ == "__main__":
    solution = max_sum_subarray_k_naive(3, [2, 1, 5, 1, 3, 2])
    print("Naive Solution: ", solution)
    solution = max_sum_subarray_k_naive(2, [2, 3, 4, 1, 5])
    print("Naive Solution: ", solution)

    solution = max_sum_subarray_k_optimal(3, [2, 1, 5, 1, 3, 2])
    print("Optimal Solution: ", solution)
    solution = max_sum_subarray_k_optimal(2, [2, 3, 4, 1, 5])
    print("Optimal Solution: ", solution)
