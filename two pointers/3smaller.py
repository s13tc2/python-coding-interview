# Given an array arr of unsorted numbers and a target sum,
# count all triplets in it such that arr[i] + arr[j] + arr[k] < target
# where i, j, and k are three different indices.
# Write a function to return the count of such triplets.

# O(N^2) time | O(N) space
def triplet_with_smaller_sum(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current = arr[i] + arr[left] + arr[right]
            if current < target:
                count += right - left
                left += 1
            else:
                right -= 1
    return count


if __name__ == "__main__":
    solution = triplet_with_smaller_sum([-1, 0, 2, 3], 3)
    print(solution)
    solution = triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)
    print(solution)

# Similar Question
# Write a function to return the list of all such triplets instead of the count. How will the time complexity change in this case?

# O(N^3) time | O(N) space
def triplet_with_smaller_sum(arr, target):
    arr.sort()
    triplets = []
    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1
        while left < right:
            current = arr[i] + arr[left] + arr[right]
            if current < target:
                for j in range(right, left, -1):
                    triplets.append([arr[i], arr[j], arr[left]])
                left += 1
            else:
                right -= 1
    return triplets


if __name__ == "__main__":
    solution = triplet_with_smaller_sum([-1, 0, 2, 3], 3)
    print(solution)
    solution = triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)
    print(solution)
