# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s,
# find the length of the longest contiguous subarray having all 1s.

# O(N) time | O(1) space
def longest_substring_replacement_one(arr, k):
    max_length = 0
    window_start = 0
    max_ones = 0

    for window_end in range(len(arr)):
        num = arr[window_end]
        if num == 1:
            max_ones += 1
        if window_end - window_start + 1 - max_ones > k:
            num = arr[window_start]
            if num == 1:
                max_ones -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)
    return max_length


if __name__ == "__main__":
    solution = longest_substring_replacement_one([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)
    print(solution)
    solution = longest_substring_replacement_one(
        [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3
    )
    print(solution)
