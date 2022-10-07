# Given the head of a Singly LinkedList, write a method to modify the LinkedList
# such that the nodes from the second half of the LinkedList are inserted alternately
#  to the nodes from the first half in reverse order.
# So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def print_list(self):
        curr = self
        while curr:
            print(str(curr.value) + " ", end="")
            curr = curr.next
        print()


# O(N) time | O(1) space
def rearrange_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev, curr = None, slow
    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    first, second = head, prev
    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    rearrange_linked_list(head)
    head.print_list()
