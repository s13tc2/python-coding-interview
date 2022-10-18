# Given a binary tree and a node, find the level order successor of the given node in the tree.
# The level order successor is the node that appears right after the given node in the level order traversal.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def find_successor(root, key):
    if not root:
        return root

    q = deque()
    q.append(root)

    while q:
        node = q.popleft()

        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

        if node.value == key:
            break

    return q[0] if q else None


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    result = find_successor(root, 3)
    if result:
        print(result.value)

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    result = find_successor(root, 9)
    if result:
        print(result.value)

    result = find_successor(root, 12)
    if result:
        print(result.value)
