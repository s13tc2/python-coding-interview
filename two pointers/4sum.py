# Given an array of unsorted numbers and a target number, find all unique quadruplets in it, whose sum is equal to the target number.

# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.

# O(N^3) time | O(N) space
def search_quadruplets(arr, target):
    arr.sort()
    quads = []
    for i in range(len(arr) - 3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        for j in range(i + 1, len(arr) - 2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue
            search_pairs(arr, target, quads, i, j)
    return quads


def search_pairs(arr, target, quads, i, j):
    left = j + 1
    right = len(arr) - 1
    while left <= right:
        current = arr[i] + arr[j] + arr[left] + arr[right]
        if current < target:
            left += 1
        elif current > target:
            right -= 1
        else:
            quads.append([arr[i], arr[j], arr[left], arr[right]])
            while left < right and arr[left] == arr[left + 1]:
                left += 1
            while left < right and arr[right] == arr[right - 1]:
                right -= 1
            left += 1
            right -= 1


if __name__ == "__main__":
    solution = search_quadruplets([4, 1, 2, -1, 1, -3], 1)
    print(solution)
