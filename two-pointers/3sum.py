# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.

# O(N^2) time | O(N) space
def search_triplets(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        left = i + 1
        right = len(arr) - 1
        while left <= right:
            current = arr[i] + arr[left] + arr[right]
            if current < 0:
                left += 1
            elif current > 0:
                right -= 1
            else:
                triplets.append([arr[i], arr[left], arr[right]])
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return triplets


# Hash Table Method
# O(N^2) time | O(N) space
def search_triplets_hash_table(arr):
    arr.sort()
    triplets = []
    for i in range(len(arr)):
        if arr[i] > 0:
            break
        if i == 0 or arr[i] != arr[i - 1]:
            search_pairs(arr, i, triplets)
    return triplets


def search_pairs(arr, i, triplets):
    j = i + 1
    seen = set()
    while j < len(arr):
        complement = -arr[i] - arr[j]
        if complement in seen:
            triplets.append([arr[i], arr[j], complement])
            while j + 1 < len(arr) and arr[j] == arr[j + 1]:
                j += 1
        seen.add(arr[j])
        j += 1


if __name__ == "__main__":
    solution = search_triplets([-3, 0, 1, 2, -1, 1, -2])
    print(solution)
    solution = search_triplets([-5, 2, -1, -2, 3])
    print(solution)
    solution = search_triplets_hash_table([-3, 0, 1, 2, -1, 1, -2])
    print(solution)
    solution = search_triplets_hash_table([-5, 2, -1, -2, 3])
    print(solution)
