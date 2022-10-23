# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

from heapq import *

# O(nlog(k)) time | O(k) space
def find_k_largest_numbers(nums, k):
    min_heap = []

    for i in range(0, k):
        heappush(min_heap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > min_heap[0]:
            heappop(min_heap)
            heappush(min_heap, nums[i])

    return min_heap


if __name__ == "__main__":
    print(
        "Here are the top K numbers: "
        + str(find_k_largest_numbers([3, 1, 5, 12, 2, 11], 3))
    )

    print(
        "Here are the top K numbers: "
        + str(find_k_largest_numbers([5, 12, 11, -1, 12], 3))
    )
