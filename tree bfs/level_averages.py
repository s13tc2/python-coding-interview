# Given a binary tree, populate an array to represent the averages of all of its levels.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


# O(n) time | O(n) space
def find_level_averages(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)
    while q:
        levelSize = len(q)
        levelSum = 0.0
        for _ in range(levelSize):
            node = q.popleft()

            levelSum += node.value

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(levelSum / levelSize)

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_averages(root)))
