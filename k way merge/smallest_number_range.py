# Given ‘M’ sorted arrays, find the smallest range that includes at least one number from each of the ‘M’ lists.

from heapq import *

# O(nlog(m)) time | O(m) space
def find_smallest_range(lists):
    rangeStart, rangeEnd = 0, float("inf")
    min_heap = []
    currentMaxNumber = 0
    for arr in lists:
        heappush(min_heap, (arr[0], arr, 0))
        currentMaxNumber = max(currentMaxNumber, arr[0])

    while len(min_heap) == len(lists):
        num, arr, i = heappop(min_heap)
        if rangeEnd - rangeStart > currentMaxNumber - num:
            rangeStart = num
            rangeEnd = currentMaxNumber

        if len(arr) > i + 1:
            heappush(min_heap, (arr[i + 1], arr, i + 1))
            currentMaxNumber = max(currentMaxNumber, arr[i + 1])
    return [rangeStart, rangeEnd]


if __name__ == "__main__":
    print(
        "Smallest range is: "
        + str(find_smallest_range([[1, 5, 8], [4, 12], [7, 8, 10]]))
    )
