# Given a binary tree, populate an array to represent its zigzag level order traversal.
# You should populate the values of all nodes of the first level from left to right,
# then right to left for the next level and keep alternating in the same manner for the following levels.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(n) space
def traverse(root):
    result = []
    if root is None:
        return result

    q = deque()
    q.append(root)
    leftToRight = True
    while q:
        levelSize = len(q)
        currentLevel = deque()
        for _ in range(levelSize):
            node = q.popleft()

            if leftToRight:
                currentLevel.append(node.value)
            else:
                currentLevel.appendleft(node.value)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(list(currentLevel))
        leftToRight = not leftToRight

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    print("Zigzag traversal: " + str(traverse(root)))
