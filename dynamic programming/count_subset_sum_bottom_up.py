# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.


def count_subsets(num, sum):
    n = len(num)

    dp = [[-1 for x in range(sum + 1)] for y in range(n)]

    for i in range(0, n):
        dp[i][0] = 1

    for j in range(1, sum + 1):
        dp[0][j] = 1 if num[0] == j else 0

    for i in range(1, n):
        for j in range(1, sum + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= num[i]:
                dp[i][j] += dp[i - 1][j - num[i]]
    return dp[n - 1][sum]


if __name__ == "__main__":
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
