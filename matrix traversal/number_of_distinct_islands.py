# You are given a 2D matrix containing only 1s (land) and 0s (water).

# An island is a connected set of 1s (land) and is surrounded by either an edge or 0s (water).
# Each cell is considered connected to other cells horizontally or vertically (not diagonally).

# Two islands are considered the same if and only if they can be translated (not rotated or reflected) to equal each other.

# Write a function to find the number of distinct islands in the given matrix.

# O(m*n) time | O(m*n) space
def findDistinctIslands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for x in range(cols)] for y in range(rows)]
    islandSet = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 1 and not visited[i][j]:
                traversal = traverseIslandDFS(matrix, visited, i, j, "O")
                islandSet.add(traversal)
    print(islandSet)
    return len(islandSet)


def traverseIslandDFS(matrix, visited, i, j, direction):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return ""
    if matrix[i][j] == 0 or visited[i][j]:
        return ""

    visited[i][j] = True

    islandTraversal = direction

    islandTraversal += traverseIslandDFS(matrix, visited, i + 1, j, "D")
    islandTraversal += traverseIslandDFS(matrix, visited, i - 1, j, "U")
    islandTraversal += traverseIslandDFS(matrix, visited, i, j + 1, "R")
    islandTraversal += traverseIslandDFS(matrix, visited, i, j - 1, "L")

    islandTraversal += "B"

    return islandTraversal


if __name__ == "__main__":
    print(
        findDistinctIslands(
            [
                [1, 1, 0, 1, 1],
                [1, 1, 0, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 1, 1, 0, 1],
                [0, 1, 1, 0, 1],
            ]
        )
    )

    print(
        findDistinctIslands(
            [[1, 1, 0, 1], [0, 1, 1, 0], [0, 0, 0, 0], [1, 1, 0, 0], [0, 1, 1, 0]]
        )
    )
