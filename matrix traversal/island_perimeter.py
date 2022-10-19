# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# There are no lakes on the island, so the water inside the island is not connected to the water around it.
# A cell is a square with a side length of 1..

# The given matrix has only one island, write a function to find the perimeter of that island.

# O(m*n) time | O(m*n) space
def findIslandPerimeter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                return islandPerimeterDFS(matrix, visited, i, j)
    return 0


def islandPerimeterDFS(matrix, visited, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return 1

    if matrix[i][j] == 0:
        return 1

    if visited[i][j]:
        return 0

    visited[i][j] = True

    edgeCount = 0
    edgeCount += islandPerimeterDFS(matrix, visited, i - 1, j)
    edgeCount += islandPerimeterDFS(matrix, visited, i + 1, j)
    edgeCount += islandPerimeterDFS(matrix, visited, i, j - 1)
    edgeCount += islandPerimeterDFS(matrix, visited, i, j + 1)

    return edgeCount


# O(m*n) time | O(1) space
def findIslandPerimeterIter(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1:
                result += 4

                if i > 0 and matrix[i - 1][j] == 1:
                    result -= 2
                if j > 0 and matrix[i][j - 1] == 1:
                    result -= 2

    return result


if __name__ == "__main__":
    print(
        findIslandPerimeterIter(
            [
                [1, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ]
        )
    )

    print(
        findIslandPerimeterIter(
            [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0]]
        )
    )
