# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# A closed island is an island that is totally surrounded by 0s (i.e., water).
# This means all horizontally and vertically connected cells of a closed island are water.
# This also means that, by definition, a closed island can't touch an edge (as then the edge cells are not connected to any water cell).

# Write a function to find the number of closed islands in the given matrix.

# O(m*n) time | O(m*n) space
def countClosedIslandsDFS(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    countClosedIslands = 0
    visited = [[False for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                if isClosedIslandDFS(matrix, visited, i, j):
                    countClosedIslands += 1
    return countClosedIslands


def isClosedIslandDFS(matrix, visited, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return False
    if matrix[i][j] == 0 or visited[i][j]:
        return True

    visited[i][j] = True
    isClosed = True

    isClosed &= isClosedIslandDFS(matrix, visited, i - 1, j)
    isClosed &= isClosedIslandDFS(matrix, visited, i + 1, j)
    isClosed &= isClosedIslandDFS(matrix, visited, i, j - 1)
    isClosed &= isClosedIslandDFS(matrix, visited, i, j + 1)

    return isClosed


if __name__ == "__main__":
    print(
        countClosedIslandsDFS(
            [
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    print(
        countClosedIslandsDFS(
            [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]
        )
    )
