# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

from heapq import *

# O(klog(m)) time | O(m) space
def find_Kth_smallest(lists, k):
    min_heap = []
    for i in range(len(lists)):
        heappush(min_heap, (lists[i][0], lists[i], 0))

    num, count = 0, 0
    while min_heap:
        num, list, i = heappop(min_heap)
        count += 1
        if count == k:
            break
        if len(list) > i + 1:
            heappush(min_heap, (list[i + 1], list, i + 1))
    return num


if __name__ == "__main__":
    print(
        "Kth smallest number is: "
        + str(find_Kth_smallest([[2, 6, 8], [3, 6, 7], [1, 3, 4]], 5))
    )
