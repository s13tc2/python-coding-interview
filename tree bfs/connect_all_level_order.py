# Given a binary tree, connect each node with its level order successor.
# The last node of each level should point to the first node of the next level.

from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None

    # tree traversal using 'next' pointer
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end="")
        current = self
        while current:
            print(str(current.value) + " ", end="")
            current = current.next


# O(n) time | O(n) space
def connect_all(root):
    if not root:
        return root

    q = deque()
    q.append(root)
    prev, curr = None, None
    while q:
        level_size = len(q)
        for _ in range(level_size):
            curr = q.popleft()
            if prev:
                prev.next = curr
            prev = curr

            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

    return root


# O(n) time | O(1) space
def connect_all_optimal(root):
    if root:
        curr = root
        last = root

    while curr:
        if curr.left:
            last.next = curr.left
            last = curr.left
        if curr.right:
            last.next = curr.right
            last = curr.right
        last.next = None
        curr = curr.next
    return root


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_optimal(root)
    root.print_tree()
