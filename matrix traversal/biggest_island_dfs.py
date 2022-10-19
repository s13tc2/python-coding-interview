# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), find the biggest island in it.
# Write a function to return the area of the biggest island.

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# O(m*n) time | O(m*n) space
def maxAreaIslandDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    biggestIslandArea = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                biggestIslandArea = max(biggestIslandArea, visitIslandDFS(matrix, i, j))
    return biggestIslandArea


def visitIslandDFS(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 0
    if matrix[i][j] == 0:
        return 0

    matrix[i][j] = 0
    area = 1

    area += visitIslandDFS(matrix, i - 1, j)
    area += visitIslandDFS(matrix, i + 1, j)
    area += visitIslandDFS(matrix, i, j - 1)
    area += visitIslandDFS(matrix, i, j + 1)
    return area


if __name__ == "__main__":
    print(
        maxAreaIslandDFS(
            [
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        )
    )
