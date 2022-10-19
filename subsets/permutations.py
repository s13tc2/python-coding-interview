# Given a set of distinct numbers, find all of its permutations.

# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

# 1. {1, 2, 3}
# 2. {1, 3, 2}
# 3. {2, 1, 3}
# 4. {2, 3, 1}
# 5. {3, 1, 2}
# 6. {3, 2, 1}

# If a set has ‘n’ distinct elements it will have n!
# n! permutations.

# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

from collections import deque

# O(n*n!) time | O(n*n!) space
def find_permutations(nums):
    num_length = len(nums)
    permutations = deque()
    permutations.append([])
    result = []
    for currentNum in nums:
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            for j in range(len(oldPermutation) + 1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNum)
                if len(newPermutation) == num_length:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    return result


def generate_permutations(nums):
    result = []
    generate_permutations_rec(nums, 0, [], result)
    return result


def generate_permutations_rec(nums, current_index, current_permutations, result):
    if current_index == len(nums):
        result.append(current_permutations)
    else:
        for i in range(len(current_permutations) + 1):
            new_permutation = list(current_permutations)
            new_permutation.insert(i, nums[current_index])
            generate_permutations_rec(nums, current_index + 1, new_permutation, result)


if __name__ == "__main__":
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))
    print("Here are all the permutations: " + str(generate_permutations([1, 3, 5])))
