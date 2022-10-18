# Find the minimum depth of a binary tree.
# The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def find_minimum_depth(root):
    # TODO: Write your code here
    if not root:
        return root
    minDepth = 0
    q = deque([root])
    while q:
        level_size = len(q)
        minDepth += 1
        for _ in range(level_size):
            node = q.popleft()
            if node.left is None and node.right is None:
                return minDepth

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return -1


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
