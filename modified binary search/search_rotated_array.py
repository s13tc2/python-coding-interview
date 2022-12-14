# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, find if a given ‘key’ is present in it.

# Write a function to return the index of the ‘key’ in the rotated array.
# If the ‘key’ is not present, return -1. You can assume that the given array does not have any duplicates.

# O(log(n)) time | O(1) space
def search_rotated_array(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        potential = arr[mid]
        leftNum = arr[start]
        rightNum = arr[end]
        if potential == key:
            return mid
        elif leftNum < potential:
            if leftNum <= key < potential:
                end = mid - 1
            else:
                start = mid + 1
        else:
            if potential < key <= rightNum:
                start = mid + 1
            else:
                end = mid - 1
    return -1


if __name__ == "__main__":
    print(search_rotated_array([10, 15, 1, 3, 8], 15))
    print(search_rotated_array([4, 5, 7, 9, 10, -1, 2], 10))
