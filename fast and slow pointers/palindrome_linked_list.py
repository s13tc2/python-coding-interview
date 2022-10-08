# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished.
# The algorithm should have O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(N) time | O(1) space
def is_palindromic_linked_list(head):
    if head is None or head.next is None:
        return head

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reverse_of_second_half = reverse(slow)
    copy_of_second_half = reverse_of_second_half

    while head and reverse_of_second_half:
        if head.value != reverse_of_second_half.value:
            return False
        head = head.next
        reverse_of_second_half = reverse_of_second_half.next

    reverse(copy_of_second_half)
    if head is None and reverse_of_second_half is None:
        return True
    return False


def reverse(head):
    prev, curr = None, head
    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


if __name__ == "__main__":
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))

    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))
