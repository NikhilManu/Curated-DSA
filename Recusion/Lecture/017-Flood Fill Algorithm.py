# Time O(m * n) | Space O(m * n)
def floodFill(image, x, y, newColor):
    if image[x][y] == newColor:
        return image
    return helper(image, x, y, image[x][y], newColor)

def helper(image, i, j, originalColor, newColor):
    if outOfBounds(image, i, j) or image[i][j] != originalColor:
        return 

    image[i][j] = newColor
    helper(image, i + 1, j, originalColor, newColor)
    helper(image, i - 1, j, originalColor, newColor)
    helper(image, i, j + 1, originalColor, newColor)
    helper(image, i, j - 1, originalColor, newColor)
    return image

def outOfBounds(image, x, y):
    return x < 0 or y < 0 or x >= len(image) or y >= len(image[0])