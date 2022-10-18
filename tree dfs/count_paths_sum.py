# Given a binary tree and a number ‘S’, find all paths in the tree such that the sum of all the node values of each path equals ‘S’.
# Please note that the paths can start or end at any node but all paths must follow direction from parent to child (top to bottom).


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n^2) time | O(n) space
def count_paths(root, S):
    return count_paths_rec(root, S, [])


def count_paths_rec(node, S, currentPath):
    if not node:
        return 0

    currentPath.append(node.value)
    pathSum, pathCount = 0, 0
    for i in range(len(currentPath) - 1, -1, -1):
        pathSum += currentPath[i]
        if pathSum == S:
            pathCount += 1

    pathCount += count_paths_rec(node.left, S, currentPath)
    pathCount += count_paths_rec(node.right, S, currentPath)

    del currentPath[-1]
    return pathCount


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))
