# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.


def count_subsets(num, sum):
    dp = [[-1 for x in range(sum + 1)] for y in range(len(num))]
    return count_subsets_rec(dp, num, sum, 0)


def count_subsets_rec(dp, num, s, index):
    n = len(num)
    if s == 0:
        return 1

    if n == 0 or index >= n:
        return 0

    if dp[index][s] == -1:
        s1 = 0
        if num[index] <= s:
            s1 = count_subsets_rec(dp, num, s - num[index], index + 1)
        s2 = count_subsets_rec(dp, num, s, index + 1)
        dp[index][s] = s1 + s2
    return dp[index][s]


if __name__ == "__main__":
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
