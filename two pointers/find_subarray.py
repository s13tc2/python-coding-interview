# Given an array with positive numbers and a positive target number,
# find all of its contiguous subarrays whose product is less than the target number.

# Input: [2, 5, 3, 10], target=30
# Output: [2], [5], [2, 5], [3], [5, 3], [10]
# Explanation: There are six contiguous subarrays whose product is less than the target.

from collections import deque

# O(N^3) time | O(N) space ignoring space for output list
def find_subarrays(arr, target):
    left = 0
    product = 1
    result = []
    for right in range(len(arr)):
        product *= arr[right]
        while product >= target and left <= right:
            product /= arr[left]
            left += 1
        temp = deque()
        for i in range(right, left - 1, -1):
            temp.append(arr[i])
            result.append(list(temp))
    return result


if __name__ == "__main__":
    solution = find_subarrays([2, 5, 3, 10], 30)
    print(solution)
