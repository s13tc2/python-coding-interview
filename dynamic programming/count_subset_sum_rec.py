# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

# O(2^n) time | O(n) space
def count_subsets(num, sum):
    return count_subset_rec(num, sum, 0)


def count_subset_rec(num, s, index):
    n = len(num)

    if s == 0:
        return 1

    if n == 0 or index >= n:
        return 0

    s1 = 0
    if num[index] <= s:
        s1 = count_subset_rec(num, s - num[index], index + 1)

    s2 = count_subset_rec(num, s, index + 1)
    return s1 + s2


if __name__ == "__main__":
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
