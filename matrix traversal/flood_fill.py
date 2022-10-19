# Any image can be represented by a 2D integer array (i.e., a matrix) where each cell represents the pixel value of the image.

# Flood fill algorithm takes a starting cell (i.e., a pixel) and a color.
# The given color is applied to all horizontally and vertically connected cells with the same color as that of the starting cell.
# Recursively, the algorithm fills cells with the new color until it encounters a cell with a different color than the starting cell.

# Given a matrix, a starting cell, and a color, flood fill the matrix.

# O(m*n) time | O(m*n) space
def floodFill(matrix, i, j, newColor):
    if matrix[i][j] != newColor:
        fillDFS(matrix, i, j, matrix[i][j], newColor)
    return matrix


def fillDFS(matrix, i, j, oldColor, newColor):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
        return
    if matrix[i][j] != oldColor:
        return

    matrix[i][j] = newColor

    fillDFS(matrix, i + 1, j, oldColor, newColor)
    fillDFS(matrix, i - 1, j, oldColor, newColor)
    fillDFS(matrix, i, j + 1, oldColor, newColor)
    fillDFS(matrix, i, j - 1, oldColor, newColor)


if __name__ == "__main__":
    print(
        floodFill(
            [
                [0, 1, 1, 1, 0],
                [0, 0, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 1, 1, 0, 0],
                [0, 0, 0, 0, 0],
            ],
            1,
            3,
            2,
        )
    )
    print(
        floodFill(
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 1, 0, 0],
            ],
            3,
            2,
            5,
        )
    )
