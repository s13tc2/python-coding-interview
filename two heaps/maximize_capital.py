# Given a set of investment projects with their respective profits, we need to find the most profitable projects. We are given an initial capital and are allowed to invest only in a fixed number of projects. Our goal is to choose projects that give us the maximum profit. Write a function that returns the maximum total capital after selecting the most profitable projects.

# We can start an investment project only when we have the required capital. Once a project is selected, we can assume that its profit has become our capital.

# Example 1:

# Input: Project Capitals=[0,1,2], Project Profits=[1,2,3], Initial Capital=1, Number of Projects=2
# Output: 6
# Explanation:

# 1. With initial capital of ‘1’, we will start the second project which will give us profit of ‘2’. Once we selected our first project, our total capital will become 3 (profit + initial capital).
# 2. With ‘3’ capital, we will select the third project, which will give us ‘3’ profit.
# After the completion of the two projects, our total capital will be 6 (1+2+3).

from heapq import *


# O(nlog(k) + klog(n)) time | O(n) space
def find_max_capital(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    for i in range(len(profits)):
        heappush(minCapitalHeap, (capital[i], i))

    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))

        if not maxProfitHeap:
            break

        availableCapital += -heappop(maxProfitHeap)[0]

    return availableCapital


if __name__ == "__main__":
    print("Maximum capital: " + str(find_max_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " + str(find_max_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))
