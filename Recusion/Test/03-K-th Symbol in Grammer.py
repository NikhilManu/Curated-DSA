# Method 1

"""
n = 1   1                               2^0
        1   0                           2^1
        1   0   0   1                   2^2
        1   0   0   1   0   1   1   0   2^(n-1) no: of columns in nth row

observations
    --> if k <= mid: // where mid is no of columns in a row by 2 
            row[n][k] is equal to row[n - 1][k] // clearly we can see this in the example
    --> if for k > mid:
            for this case we dont have any previous values but they are complement of bits upto mid values ie
            row[n][k] is equal to !row[n - 1][k - mid]

            eg n = 4 and k = 5  (row[4][5] = !row[3][5-4] = !row[3][1] = !1 = 0)
"""
def kthValue(n, k):
    return int(helper(n, k))

def helper(n, k):
    if n == 1 and k == 1:
        return 1

    columns = 2 ** (n - 1)
    mid = columns // 2
    if k <= mid:
        return helper(n - 1, k)
    else:
        return not helper(n - 1, k - mid)

# Method 2

"""
n = 1   1                               2^0
        1   0                           2^1
        1   0   0   1                   2^2
        1   0   0   1   0   1   1   0   2^(n-1) no: of columns in nth row

Observations:
    --> if we notice each of the odd position has the value of the parent
"""
def kthValue(n, k):
    return helper(n, k)

def helper(n, k):
    if k == 1:
        return 1

    oddPosition = k % 2 == 1
    parent = helper(n - 1, (k + 1) // 2) if oddPosition else helper(n - 1, k // 2) # odd position means cant divide by 2, so adding one would give the corrent parent

    if parent == 1:
        return 1 if oddPosition else 0
    else:
        return 0 if oddPosition else 1