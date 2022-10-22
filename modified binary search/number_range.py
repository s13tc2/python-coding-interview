# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’.
# The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

# O(log(n)) time | O(1) space
def find_range(arr, key):
    finalRange = [-1, -1]
    alteredBinarySearch(arr, key, 0, len(arr) - 1, finalRange, True)
    alteredBinarySearch(arr, key, 0, len(arr) - 1, finalRange, False)
    return finalRange


def alteredBinarySearch(arr, key, start, end, finalRange, goLeft):
    while start <= end:
        mid = start + (end - start) // 2
        potential = arr[mid]
        if potential < key:
            start = mid + 1
        elif potential > key:
            end = mid - 1
        else:
            if goLeft:
                if mid == 0 or arr[mid] != arr[mid - 1]:
                    finalRange[0] = mid
                    break
                else:
                    end = mid - 1
            else:
                if mid == len(arr) - 1 or arr[mid] != arr[mid + 1]:
                    finalRange[1] = mid
                    break
                else:
                    start = mid + 1
    return [-1, -1]


if __name__ == "__main__":
    print(find_range([4, 6, 6, 6, 9], 6))
    print(find_range([1, 3, 8, 10, 15], 10))
    print(find_range([1, 3, 8, 10, 15], 12))
