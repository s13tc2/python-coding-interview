# Given a 2D array (i.e., a matrix) containing only 1s (land) and 0s (water), count the number of islands in it.

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# O(m*n) time | O(m*n) space
def countIslandsDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    totalIslands = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                totalIslands += 1
                visitIslandDFS(matrix, i, j)
    return totalIslands


def visitIslandDFS(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if matrix[i][j] == 0:
        return

    matrix[i][j] = 0

    visitIslandDFS(matrix, i - 1, j)
    visitIslandDFS(matrix, i + 1, j)
    visitIslandDFS(matrix, i, j - 1)
    visitIslandDFS(matrix, i, j + 1)


if __name__ == "__main__":
    print(
        countIslandsDFS(
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
        countIslandsDFS(
            [
                [1, 1, 1, 0, 0],
                [0, 1, 0, 0, 1],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ]
        )
    )
