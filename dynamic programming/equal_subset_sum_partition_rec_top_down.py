# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# O(n*s) time | O(n*s) space
def can_partition(num):
    s = sum(num)
    if s % 2 != 0:
        return False
    dp = [[-1 for x in range(int(s / 2) + 1)] for y in range(len(num))]
    return True if can_partition_rec(dp, num, int(s / 2), 0) == 1 else False


def can_partition_rec(dp, num, s, index):
    n = len(num)

    if s == 0:
        return 1

    if n == 0 or index >= n:
        return 0

    if dp[index][s] == -1:
        if num[index] <= s:
            if can_partition_rec(dp, num, s - num[index], index + 1) == 1:
                dp[index][s] = 1
                return 1

        dp[index][s] = can_partition_rec(dp, num, s, index + 1)
    return dp[index][s]


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))
