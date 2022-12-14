# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]

# Input: [1, 5, 3, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3]

# O(n*2^n) time | O(n*2^n) space
def find_subsets(nums):
    list.sort(nums)
    subsets = []
    subsets.append([])
    start, end = 0, 0
    for i in range(len(nums)):
        start = 0
        if i > 0 and nums[i] == nums[i - 1]:
            start = end + 1
        end = len(subsets) - 1
        for j in range(start, end + 1):
            set1 = list(subsets[j])
            set1.append(nums[i])
            subsets.append(set1)
    return subsets


if __name__ == "__main__":
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))
