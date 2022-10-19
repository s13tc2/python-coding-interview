# Given a number ‘n’, write a function to return all structurally unique Binary Search Trees (BST) that can store values 1 to ‘n’?

# Input: 2
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 2 structurally unique BSTs storing all numbers from 1 to 2:

# Input: 3
# Output: List containing root nodes of all structurally unique BSTs.
# Explanation: Here are the 5 structurally unique BSTs storing all numbers from 1 to 3:


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n*2^n) time | O(2^n) space
def find_unique_trees(n):
    return find_unique_tree_rec(1, n)


def find_unique_tree_rec(start, end):
    result = []

    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left = find_unique_tree_rec(start, i - 1)
        right = find_unique_tree_rec(i + 1, end)
        for l in left:
            for r in right:
                root = TreeNode(i)
                root.left = l
                root.right = r
                result.append(root)
    return result


if __name__ == "__main__":
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))
