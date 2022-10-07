# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(N) time | O(1) space
def find_cycle_start(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            cycle_length = calculate_cycle_length(slow)
            break
    return find_start(head, cycle_length)


def calculate_cycle_length(slow):
    curr = slow
    length = 0
    while True:
        curr = curr.next
        length += 1
        if curr == slow:
            break
    return length


def find_start(head, cycle_length):
    p1, p2 = head, head
    while cycle_length > 0:
        p2 = p2.next
        cycle_length -= 1
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next
    return p1


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))
