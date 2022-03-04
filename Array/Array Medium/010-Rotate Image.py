# Time O(N ^ 2) | Space O(N ^ 2)

# Not Accepted In Interview
"""
Create a matrix of size N * N 

[ 
    [1, 2, 3],
    [4, 5, 6],          ===>     Here Last row will become the first Column ...so on... first row will become the last Column
    [7, 8, 9]
]
"""

# Time O(N ^ 2) | Space O(1)

def RotateImage(matrix):
    transpose(matrix) # Transpose means all the row will become Column
    reverse(matrix) # Reversing the values of each row

def transpose(matrix):
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def reverse(matrix):
    for i in range(len(matrix)):
        left, right = 0, len(matrix[i]) - 1
        while left < right:
            matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            left += 1; right -= 1