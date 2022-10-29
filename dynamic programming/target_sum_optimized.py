# You are given a set of positive numbers and a target sum ‘S’.
# Each number should be assigned either a ‘+’ or ‘-’ sign.
# We need to find the total ways to assign symbols to make the sum of the numbers equal to the target ‘S’.

# O(n*s) time | O(s) space
def find_target_subsets(num, s):
    totalSum = sum(num)
    if totalSum < s or (s + totalSum) % 2 != 0:
        return 0

    return count_subsets(num, (s + totalSum) // 2)


def count_subsets(num, s):
    n = len(num)

    dp = [-1 for x in range(s + 1)]
    dp[0] = 1

    for j in range(1, s + 1):
        dp[j] = 1 if num[0] == j else 0

    for i in range(1, n):
        for j in range(s, -1, -1):
            if j >= num[i]:
                dp[j] += dp[j - num[i]]
    return dp[s]


if __name__ == "__main__":
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))
