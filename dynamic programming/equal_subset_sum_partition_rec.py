# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# O(2^n) time | O(2^n) space
def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    return can_partition_rec(num, int(s / 2), 0)


def can_partition_rec(num, s, index):
    n = len(num)
    if s == 0:
        return True

    if n == 0 or index >= n:
        return False

    if num[index] <= s:
        if can_partition_rec(num, s - num[index], index + 1):
            return True

    return can_partition_rec(num, s, index + 1)


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))
