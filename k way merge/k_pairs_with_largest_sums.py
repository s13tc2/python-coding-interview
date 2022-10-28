# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.

from heapq import *

# O(nmlog(k)) time | O(k) space
def find_k_largest_pairs(nums1, nums2, k):
    min_heap = []
    result = []
    for i in range(len(nums1)):
        for j in range(len(nums2)):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))

    for num, i, j in min_heap:
        result.append([nums1[i], nums2[j]])
    return result


# O(k^2log(k)) time | O(k) space
def find_k_largest_pairs_optimal(nums1, nums2, k):
    min_heap = []
    result = []
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(min_heap) < k:
                heappush(min_heap, (nums1[i] + nums2[j], i, j))
            else:
                if nums1[i] + nums2[j] < min_heap[0][0]:
                    break
                else:
                    heappop(min_heap)
                    heappush(min_heap, (nums1[i] + nums2[j], i, j))

    for num, i, j in min_heap:
        result.append([nums1[i], nums2[j]])
    return result


if __name__ == "__main__":
    print(
        "Pairs with largest sum are: "
        + str(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))
    )
    print(
        "Pairs with largest sum are: "
        + str(find_k_largest_pairs_optimal([9, 8, 2], [6, 3, 1], 3))
    )
