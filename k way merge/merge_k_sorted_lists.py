# Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.


class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(nlog(k)) time | O(1) space
def merge_lists(lists):
    amount = len(lists)
    interval = 1
    while interval < amount:
        for i in range(0, amount - interval, interval * 2):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0] if amount > 0 else None


def mergeTwoLists(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.value <= l2.value:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 if l1 is not None else l2
    return dummy.next


if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    print("Here are the elements form the merged list: ", end="")
    while result != None:
        print(str(result.value) + " ", end="")
        result = result.next
