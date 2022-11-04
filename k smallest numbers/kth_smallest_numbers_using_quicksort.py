# Given an unsorted array of numbers, find Kth smallest number in it.

from heapq import *

# O(n) time | O(n) space 
# O(n^2) time worst case | O(n) space
def find_kth_smallest_number(nums, k):
    return find_kth_smallest_number_rec(nums, k, 0, len(nums)-1)

def find_kth_smallest_number_rec(nums, k, start, end):
    p = partition(nums, start, end)

    if p == k - 1:
        return nums[p]
    
    if p > k - 1:
        return find_kth_smallest_number_rec(nums, k, start, p-1)
    
    return find_kth_smallest_number_rec(nums, k, p+1, end)

def partition(nums, low, high):
    if low == high:
        return low
    
    pivot = nums[high]
    for i in range(low, high):
        if nums[i] < pivot:
            nums[low], nums[i] = nums[i], nums[low]
            low += 1
    
    nums[low], nums[high] = nums[high], nums[low]
    return low

if __name__ == "__main__":
    print("Kth smallest number is: " +
            str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 3)))

    print("Kth smallest number is: " +
            str(find_kth_smallest_number([1, 5, 12, 2, 11, 5], 4)))

    print("Kth smallest number is: " +
            str(find_kth_smallest_number([5, 12, 11, -1, 12], 3)))