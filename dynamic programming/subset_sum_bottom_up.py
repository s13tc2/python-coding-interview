# Given a set of positive numbers, determine if a subset exists whose sum is equal to a given number ‘S’.

# O(n*c) time | O(n*c) space
def can_partition(num, sum):
    n = len(num)

    if sum % 2 != 0:
        return False

    dp = [[False for x in range(sum + 1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(1, sum + 1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, sum + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]
    return dp[n - 1][sum]


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
