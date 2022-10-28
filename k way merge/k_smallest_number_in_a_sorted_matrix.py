# Given an N*N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

from heapq import *

# O(min(k,n) + klog(n)) | O(n) space
def find_Kth_smallest(matrix, k):
    min_heap = []
    for i in range(len(matrix)):
        heappush(min_heap, (matrix[i][0], matrix[i], 0))

    num = 0
    count = 0
    while min_heap:
        num, row, i = heappop(min_heap)
        count += 1
        if count == k:
            break
        if len(min_heap) > i + 1:
            heappush(min_heap, (row[i + 1], row, i + 1))
    return num


# O(n(log_max-log_min)) time | O(1) space
def find_Kth_smallest_binary_search(matrix, k):
    n = len(matrix) - 1
    start, end = matrix[0][0], matrix[n - 1][n - 1]
    while start < end:
        mid = start + (end - start) // 2
        smaller, larger = (matrix[0][0], matrix[n - 1][n - 1])

        count, smaller, larger = count_less_equal(matrix, mid, smaller, larger)

        if count == k:
            return smaller
        if count < k:
            start = larger
        else:
            end = smaller
    return start


def count_less_equal(matrix, mid, smaller, larger):
    count, n = 0, len(matrix)
    row, col = n - 1, 0
    while row >= 0 and col < n:
        if matrix[row][col] > mid:
            larger = min(larger, matrix[row][col])
            row -= 1
        else:
            smaller = max(smaller, matrix[row][col])
            count += row + 1
            col += 1
    return count, smaller, larger


if __name__ == "__main__":
    print(
        "Kth smallest number is: "
        + str(find_Kth_smallest([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))
    )
    print(
        "Kth smallest number is: "
        + str(find_Kth_smallest_binary_search([[2, 6, 8], [3, 7, 10], [5, 8, 11]], 5))
    )
