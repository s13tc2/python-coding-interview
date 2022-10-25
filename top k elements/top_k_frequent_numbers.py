# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

from heapq import *
from collections import Counter

# O(nlog(k)) time | O(n) space
def find_k_frequent_numbers(nums, k):
    num_freq = {}
    for num in nums:
        num_freq[num] = num_freq.get(num, 0) + 1

    min_heap = []
    for num, freq in num_freq.items():
        heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heappop(min_heap)

    topNumbers = []
    for i in range(0, k):
        topNumbers.append(heappop(min_heap)[1])
    return topNumbers


# O(n) time | O(n) space
def find_k_frequent_numbers_optimal(nums, k):
    bucket = [[] for _ in range(len(nums) + 1)]
    count = Counter(nums).items()
    for num, freq in count:
        bucket[freq].append(num)
    flatten_list = [item for sublist in bucket for item in sublist]
    return flatten_list[::-1][:k]


if __name__ == "__main__":
    print(
        "Here are the K frequent numbers: "
        + str(find_k_frequent_numbers_optimal([1, 3, 5, 12, 11, 12, 11], 2))
    )

    print(
        "Here are the K frequent numbers: "
        + str(find_k_frequent_numbers_optimal([5, 12, 11, 3, 11], 2))
    )
