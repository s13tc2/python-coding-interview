# Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum.

# A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
# The path must contain at least one node.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space
def find_maximum_path_sum(root):
    max_path = float("-inf")

    def get_max_gain(root):
        nonlocal max_path
        if not root:
            return 0

        gain_on_left = max(get_max_gain(root.left), 0)
        gain_on_right = max(get_max_gain(root.right), 0)

        current_max_path = root.value + gain_on_left + gain_on_right
        max_path = max(current_max_path, max_path)
        return root.value + max(gain_on_left, gain_on_right)

    get_max_gain(root)
    return max_path


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(find_maximum_path_sum(root)))
