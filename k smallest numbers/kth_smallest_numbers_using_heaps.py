# Given an unsorted array of numbers, find Kth smallest number in it.

from heapq import *

# O(nlog(k)) time | O(k) space
def find_kth_smallest_number(nums, k):
    max_heap = []

    for i in range(k):
        heappush(max_heap, -nums[i])
    
    for i in range(k, len(nums)):
        if -nums[i] > max_heap[0]:
            heappop(max_heap)
            heappush(max_heap, -nums[i])
    
    return -max_heap[0]

if __name__ == "__main__":
    print("Kth smallest number is: " +
            str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    print("Kth smallest number is: " +
            str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
            str(find_kth_smallest_number([5, 12, 11, -1, 12], 3)))