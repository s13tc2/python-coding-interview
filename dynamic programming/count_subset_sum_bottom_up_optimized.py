def count_subsets(num, sum):
    n = len(num)
    dp = [-1 for x in range(sum + 1)]
    dp[0] = 1

    for s in range(1, sum + 1):
        dp[s] = 1 if num[0] == s else 0

    for i in range(1, n):
        for s in range(sum, -1, -1):
            if s >= num[i]:
                dp[s] += dp[s - num[i]]
    return dp[sum]


if __name__ == "__main__":
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
