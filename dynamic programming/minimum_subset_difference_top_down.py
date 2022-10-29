# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.


def can_partition(num):
    s = sum(num)
    dp = [[-1 for x in range(s + 1)] for y in range(len(num))]
    return can_partition_rec(dp, num, 0, 0, 0)


def can_partition_rec(dp, num, index, s1, s2):
    if index == len(num):
        return abs(s1 - s2)

    if dp[index][s1] == -1:
        d1 = can_partition_rec(dp, num, index + 1, s1 + num[index], s2)

        d2 = can_partition_rec(dp, num, index + 1, s1, s2 + num[index])

        dp[index][s1] = min(d1, d2)
    return dp[index][s1]


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))
