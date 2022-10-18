# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end=" ")
            temp = temp.next
        print()


# O(n) time | O(1) space
def reverse_alternate_k_elements(head, k):
    prev, curr = None, head
    while curr:
        last_node_of_first_part = prev
        last_node_of_sublist = curr
        i = 0

        while curr and i < k:
            curr.next, prev, curr = prev, curr, curr.next
            i += 1

        if last_node_of_first_part is not None:
            last_node_of_first_part.next = prev
        else:
            head = prev

        last_node_of_sublist.next = curr
        i = 0
        while curr and i < k:
            prev, curr = curr, curr.next
            i += 1

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = reverse_alternate_k_elements(head, 2)
    print("Nodes of reversed LinkedList are: ", end="")
    result.print_list()
