# Given an array of sorted numbers and a target sum, find a pair in the array whose sum is equal to the given target.

# Write a function to return the indices of the two numbers (i.e. the pair) such that they add up to the given target.

# Brute Force Method
# O(nlog(n)) time | O(1) space
def pair_sum_naive(arr, target):
    for i in range(len(arr) - 1):
        first = arr[i]
        for j in range(i + 1, len(arr)):
            second = arr[j]
            if first + second == target:
                return [i, j]
    return [-1, -1]


# Hash Table Method
# O(N) time | O(N) space
def pair_sum_hash_table(arr, target):
    seen = {}
    for i in range(len(arr)):
        potential = target - arr[i]
        if potential in seen:
            return [seen[potential], i]
        else:
            seen[arr[i]] = i
    return [-1, -1]


# Binary Search Method
# O(N) time | O(1) space
def pair_sum_optimal(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        current = arr[start] + arr[end]
        if current == target:
            return [start, end]
        elif current < target:
            start += 1
        else:
            end -= 1
    return [-1, -1]


if __name__ == "__main__":
    solution = pair_sum_optimal([1, 2, 3, 4, 6], 6)
    print(solution)
    solution = pair_sum_optimal([2, 5, 9, 11], 11)
    print(solution)
