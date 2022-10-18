# Given a binary tree, return an array containing nodes in its right view.
# The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def tree_right_view(root):
    result = []
    if not root:
        return root
    q = deque([root])
    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()

            if i == level_size - 1:
                result.append(node)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.value) + " ", end="")
