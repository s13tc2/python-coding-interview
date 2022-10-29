def find_target_subsets(num, s):
    totalSum = sum(num)

    if totalSum < s or (s + totalSum) % 2 == 1:
        return 0

    return count_subsets(num, (s + totalSum) // 2)


def count_subsets(num, s):
    n = len(num)
    dp = [[0 for x in range(s + 1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for s in range(1, s + 1):
        dp[0][s] = 1 if num[0] == s else 0

    for i in range(1, n):
        for s in range(1, s + 1):
            dp[i][s] = dp[i - 1][s]
            if s >= num[i]:
                dp[i][s] += dp[i - 1][s - num[i]]
    return dp[n - 1][s]


if __name__ == "__main__":
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
