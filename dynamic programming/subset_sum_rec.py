# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

# O(2^n) time | O(2^n) space
def can_partition(num, sum):
    if sum % 2 != 0:
        return False

    return can_partition_rec(num, sum, 0)


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
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
