# Given two integer arrays to represent weights and profits of ‘N’ items,
# we need to find a subset of these items which will give us maximum profit
# such that their cumulative weight is not more than a given number ‘C.’
# Each item can only be selected once, which means either we put an item in the knapsack or we skip it.

# O(m*n) time | O(m*n) space
def solve_knapsack(profits, weights, capacity):
    dp = [[-1 for x in range(capacity + 1)] for y in range(len(profits))]
    return knapsack_rec(dp, profits, weights, capacity, 0)


def knapsack_rec(dp, profits, weights, capacity, currentIndex):
    n = len(profits)
    if capacity <= 0 or currentIndex >= len(profits):
        return 0

    if dp[currentIndex][capacity] != -1:
        return dp[currentIndex][capacity]

    p1 = 0
    if weights[currentIndex] <= capacity:
        p1 = profits[currentIndex] + knapsack_rec(
            dp, profits, weights, capacity - weights[currentIndex], currentIndex + 1
        )
    p2 = knapsack_rec(dp, profits, weights, capacity, currentIndex + 1)
    dp[currentIndex][capacity] = max(p1, p2)
    return dp[currentIndex][capacity]


if __name__ == "__main__":
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
