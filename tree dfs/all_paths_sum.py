# Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n^2) time | O(n) space
def find_paths(root, sum):
    allPaths = []
    find_paths_rec(root, sum, [], allPaths)
    return allPaths


def find_paths_rec(node, s, currentPath, allPaths):
    if node is None:
        return

    currentPath.append(node.value)

    if node.value == s and node.left is None and node.right is None:
        allPaths.append(list(currentPath))
    else:
        find_paths_rec(node.left, s - node.value, currentPath, allPaths)
        find_paths_rec(node.right, s - node.value, currentPath, allPaths)

    del currentPath[-1]


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + ": " + str(find_paths(root, sum)))
