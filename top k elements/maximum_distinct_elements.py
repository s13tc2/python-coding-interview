# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

from heapq import *

# O(nlog(k) + klog(k)) time | O(n) space
def find_maximum_distinct_elements(nums, k):
    distinct_element_count = 0
    num_freq = {}

    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    min_heap = []
    for num, freq in num_freq.items():
        if freq == 1:
            distinct_element_count += 1
        else:
            heappush(min_heap, (freq, num))

    while min_heap and k > 0:
        freq, num = heappop(min_heap)
        k -= freq - 1
        if k > 0:
            distinct_element_count += 1

    if k > 0:
        distinct_element_count -= k

    return distinct_element_count


if __name__ == "__main__":
    print(
        "Maximum distinct numbers after removing K numbers: "
        + str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2))
    )
    print(
        "Maximum distinct numbers after removing K numbers: "
        + str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3))
    )
    print(
        "Maximum distinct numbers after removing K numbers: "
        + str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], 2))
    )
