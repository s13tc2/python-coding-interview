# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of elements in both subsets is equal.

# O(n*s) time | O(n*s) space
def can_partition(num):
    s = sum(num)

    if s % 2 != 0:
        return False

    n = len(num)

    dp = [[False for x in range(s + 1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(1, s + 1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, s + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    return dp[n - 1][s]


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))
