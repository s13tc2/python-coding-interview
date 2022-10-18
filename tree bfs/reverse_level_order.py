# Given a binary tree, populate an array to represent its level-by-level traversal in reverse order,
# i.e., the lowest level comes first. You should populate the values of all nodes in each level from left to right in separate sub-arrays.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def traverse(root):
    result = deque()
    if not root:
        return root
    q = deque()
    q.append(root)
    while q:
        level_size = len(q)
        current_level = []
        for _ in range(level_size):
            node = q.popleft()
            current_level.append(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        result.appendleft(current_level)
    return list(result)


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Reverse level order traversal: " + str(traverse(root)))
