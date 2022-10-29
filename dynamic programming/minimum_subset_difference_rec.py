# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

# O(2^n) time | O(n) space
def can_partition(num):
    return can_partition_rec(num, 0, 0, 0)


def can_partition_rec(num, index, s1, s2):
    if index == len(num):
        return abs(s1 - s2)

    d1 = can_partition_rec(num, index + 1, s1 + num[index], s2)
    d2 = can_partition_rec(num, index + 1, s1, s2 + num[index])
    return min(d1, d2)


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))
