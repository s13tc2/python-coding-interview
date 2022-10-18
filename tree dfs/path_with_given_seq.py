# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# O(n) time | O(h) space
def find_path(root, sequence):
    return find_path_rec(root, sequence, 0)


def find_path_rec(node, sequence, seqIdx):
    if not node:
        return False

    seqLen = len(sequence)
    if seqIdx >= seqLen or sequence[seqIdx] != node.value:
        return False

    if node.left is None and node.right is None and seqIdx == seqLen - 1:
        return True

    return find_path_rec(node.left, sequence, seqIdx + 1) or find_path_rec(
        node.right, sequence, seqIdx + 1
    )


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))
