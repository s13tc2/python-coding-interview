# Given a set with distinct elements, find all of its distinct subsets.

# Input: [1, 3]
# Output: [], [1], [3], [1,3]

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]

# O(n*2^n) time | O(n*2^n) space
def find_subsets(nums):
    subsets = []
    subsets.append([])
    for num in nums:
        n = len(subsets)
        for i in range(n):
            set1 = list(subsets[i])
            set1.append(num)
            subsets.append(set1)
    return subsets


if __name__ == "__main__":
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))
