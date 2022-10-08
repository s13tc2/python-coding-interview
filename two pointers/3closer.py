# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible,
# return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Input: [-1, 0, 2, 3], target=3
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

# O(N^2) time | O(N) space
def triplet_sum_close_to_target(arr, target):
    arr.sort()
    smallest_diff = float("inf")
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current = arr[i] + arr[left] + arr[right]
            if abs(smallest_diff) > abs(target - current):
                smallest_diff = target - current
            elif current < target:
                left += 1
            elif current > target:
                right -= 1
        if smallest_diff == 0:
            break
    return target - smallest_diff


if __name__ == "__main__":
    solution = triplet_sum_close_to_target([-2, 0, 1, 2], 2)
    print(solution)
    solution = triplet_sum_close_to_target([-3, -1, 1, 2], 1)
    print(solution)
    solution = triplet_sum_close_to_target([1, 0, 1, 1], 100)
    print(solution)
