# Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space or O(n) worst case when tree is a linked list
def has_path_rec(root, sum):
    if not root:
        return False

    sum -= root.value
    if root.left is None and root.right is None and sum == 0:
        return True

    return has_path(root.left, sum) or has_path(root.right, sum)


# O(n) time | O(h) space
def has_path_iter(root, sum):
    stack = [(root, sum - root.value)]
    while stack:
        node, s = stack.pop()
        if node.left is None and node.right is None and s == 0:
            return True
        if node.left:
            stack.append((node.left, s - node.left.value))
        if node.right:
            stack.append((node.right, s - node.right.value))
    return False


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path_iter(root, 23)))
    print("Tree has path: " + str(has_path_iter(root, 16)))
