# Given a binary tree where each node can only have a digit (0-9) value, each root-to-leaf path will represent a number.
# Find the total sum of all the numbers represented by all paths.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space
def find_sum_of_path_numbers(root):
    return find_root_to_leaf(root, 0)


def find_root_to_leaf(node, pathSum):
    if node is None:
        return 0

    pathSum = 10 * pathSum + node.value

    if node.left is None and node.right is None:
        return pathSum

    return find_root_to_leaf(node.left, pathSum) + find_root_to_leaf(
        node.right, pathSum
    )


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))
