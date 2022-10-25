# Given a sorted number array and two integers ‘K’ and ‘X’, find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. ‘X’ is not necessarily present in the array.
from heapq import *

# O(klog(k) + log(n)) | O(k) space
def find_closest_elements(arr, K, X):
    index = binary_search(arr, X)
    low, high = index - K, index + K
    low, high = max(low, 0), min(high, len(arr) - 1)

    min_heap = []
    for i in range(low, high + 1):
        heappush(min_heap, (abs(K - arr[i]), arr[i]))

    result = []
    for i in range(K):
        result.append(heappop(min_heap)[1])
    result.sort()
    return result


def binary_search(arr, key):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    if start > 0:
        return start - 1
    return start


if __name__ == "__main__":
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6))
    )
    print(
        "'K' closest numbers to 'X' are: "
        + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10))
    )
