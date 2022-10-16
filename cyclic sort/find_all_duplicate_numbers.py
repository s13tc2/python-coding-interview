# We are given an unsorted array containing n numbers taken from the range 1 to n.
# The array has some numbers appearing twice, find all these duplicate numbers using constant space.

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]

# O(n) time | O(1) space
def find_all_duplicates(nums):
    i = 0
    while i < len(nums):
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    duplicateNumbers = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicateNumbers.append(nums[i])

    return duplicateNumbers


if __name__ == "__main__":
    print(find_all_duplicates([3, 4, 4, 5, 5]))
    print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))
