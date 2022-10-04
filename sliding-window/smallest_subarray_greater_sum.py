# Given an array of positive integers and a number ‘S,’ find the length of the smallest contiguous subarray
# whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.

# Input: [2, 1, 5, 2, 3, 2], S=7
# Output: 2
# Explanation: The smallest subarray with a sum greater than or equal to ‘7’ is [5, 2].

# O(N) time | O(1) space
def smallest_subarray_sum(s, arr):
    window_sum = 0
    window_start = 0
    min_length = float("inf")

    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    if min_length == float("inf"):
        return 0
    return min_length


if __name__ == "__main__":
    solution = smallest_subarray_sum(7, [2, 1, 5, 2, 3, 2])
    print(solution)
    solution = smallest_subarray_sum(8, [3, 4, 1, 1, 6])
    print(solution)
    solution = smallest_subarray_sum(8, [2, 1, 5, 2, 3, 2])
    print(solution)
