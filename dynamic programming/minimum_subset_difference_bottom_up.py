# Given a set of positive numbers, partition the set into two subsets with minimum difference between their subset sums.

# O(n*s) time | O(n*s) space
def can_partition(num):
    s = sum(num)
    n = len(num)
    dp = [[False for x in range(int(s / 2) + 1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = True

    for j in range(1, int(s / 2) + 1):
        dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, int(s / 2) + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    s1 = 0
    for i in range(int(s / 2), -1, -1):
        if dp[n - 1][i]:
            s1 = i
            break
    s2 = s - s1
    return abs(s2 - s1)


if __name__ == "__main__":
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))
