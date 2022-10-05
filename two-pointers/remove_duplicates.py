# Given an array of sorted numbers, remove all duplicate number instances from it in-place, such that each element appears only once.
# The relative order of the elements should be kept the same and you should not use any extra space so that that the solution have a space complexity of O(1).

# Move all the unique elements at the beginning of the array and after moving return the length of the subarray that has no duplicate in it.

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].

# O(N) time | O(1) space
def remove_duplicates(arr):
    left = 0
    for right in range(len(arr)):
        if arr[left] != arr[right]:
            left += 1
            arr[left] = arr[right]
    return left + 1


# Similar Question
# Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.

# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].

# O(N) time | O(1) space
def remove_element(arr, key):
    left = 0
    for right in range(len(arr)):
        if arr[right] != key:
            arr[left] = arr[right]
            left += 1
    return left


if __name__ == "__main__":
    solution = remove_duplicates([2, 3, 3, 3, 6, 9, 9])
    print(solution)
    solution = remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)
    print(solution)
    solution = remove_element([2, 11, 2, 2, 1], 2)
    print(solution)
