# You are given a 2D matrix containing different characters, you need to find if there exists any cycle consisting of the same character in the matrix.

# A cycle is a path in the matrix that starts and ends at the same cell and has four  or more cells.
# From a given cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left, or right), if it has the same character value of the current cell.

# Write a function to find if the matrix has a cycle.

# O(m*n) time | O(m*n) space
def hasCycle(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    visited = [[False for x in range(cols)] for y in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if not visited[i][j]:
                if containsCycleDFS(matrix, visited, matrix[i][j], i, j, -1, -1):
                    return True
    return False


def containsCycleDFS(matrix, visited, startChar, i, j, prevI, prevJ):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix):
        return False
    if matrix[i][j] != startChar:
        return False
    if visited[i][j]:
        return True

    visited[i][j] = True

    if i + 1 != prevI and containsCycleDFS(matrix, visited, startChar, i + 1, j, i, j):
        return True
    if i - 1 != prevI and containsCycleDFS(matrix, visited, startChar, i - 1, j, i, j):
        return True
    if j + 1 != prevJ and containsCycleDFS(matrix, visited, startChar, i, j + 1, i, j):
        return True
    if j - 1 != prevJ and containsCycleDFS(matrix, visited, startChar, i, j - 1, i, j):
        return True

    return False


if __name__ == "__main__":
    print(
        hasCycle(
            [
                ["a", "a", "a", "a"],
                ["b", "a", "c", "a"],
                ["b", "a", "c", "a"],
                ["b", "a", "a", "a"],
            ]
        )
    )

    print(
        hasCycle(
            [
                ["a", "a", "a", "a"],
                ["a", "b", "b", "a"],
                ["a", "b", "a", "a"],
                ["a", "a", "a", "c"],
            ]
        )
    )

    print(
        hasCycle(
            [
                ["a", "b", "e", "b"],
                ["b", "b", "b", "b"],
                ["b", "c", "c", "d"],
                ["c", "c", "d", "d"],
            ]
        )
    )
