# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

from collections import deque

# O(m*n) time | O(min(m, n))
def countIslandsBFS(matrix):
    totalIslands = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                totalIslands += 1
                visitIslandsBFS(matrix, i, j)
    return totalIslands


def visitIslandsBFS(matrix, i, j):
    neighbors = deque([(i, j)])
    while neighbors:
        row, col = neighbors.popleft()

        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            continue
        if matrix[row][col] == 0:
            continue

        matrix[row][col] = 0

        neighbors.extend([(row + 1, col)])
        neighbors.extend([(row - 1, col)])
        neighbors.extend([(row, col + 1)])
        neighbors.extend([(row, col - 1)])


if __name__ == "__main__":
    print(
        countIslandsBFS(
            [
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )
    print(
        countIslandsBFS(
            [
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        )
    )
