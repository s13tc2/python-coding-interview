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
def rotate(head, rotations):
    lastElement = head
    length = 1
    while lastElement.next:
        lastElement = lastElement.next
        length += 1
    lastElement.next = head
    temp = head
    k = rotations % length
    for _ in range(length - k - 1):
        temp = temp.next
    answer = temp.next
    temp.next = None
    return answer


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("Nodes of original LinkedList are: ", end="")
    head.print_list()
    result = rotate(head, 3)
    print("Nodes of rotated LinkedList are: ", end="")
    result.print_list()
