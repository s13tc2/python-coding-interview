# Given a Bitonic array, find if a given ‘key’ is present in it.
# An array is considered bitonic if it is monotonically increasing and then monotonically decreasing.
# Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

from search_sorted_infinite_array import binary_search

# O(log(n)) time | O(1) space
def search_bitonic_array(arr, key):
    max_index = find_max(arr, key)
    key_index = binary_search(arr, key, 0, max_index)
    if key_index != -1:
        return max_index
    return binary_search(arr, key, max_index + 1, len(arr) - 1)


def find_max(arr, key):
    start, end = 0, len(arr) - 1
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < arr[mid + 1]:
            start = mid + 1
        else:
            end = mid
    return start


def binary_search(arr, key, start, end):
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[start] < arr[end]:
            if arr[mid] < key:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if arr[mid] < key:
                end = mid - 1
            else:
                start = mid + 1

    return -1


if __name__ == "__main__":
    print(search_bitonic_array([1, 3, 8, 4, 3], 4))
    print(search_bitonic_array([3, 8, 3, 1], 8))
    print(search_bitonic_array([1, 3, 8, 12], 12))
    print(search_bitonic_array([10, 9, 8], 10))
