# Time O(2 ^ n) | Space O(N)
def findSubsetsThatSumToK(arr, k) :
    result = []
    helper(arr, k, 0, 0, [], result)
    return result

def helper(arr, k, i, curSum, comb, result):
    if i == len(arr) and curSum == k: # if i == len(arr) is not added, look at wrong approach 2 to understand
        result.append(comb)
        return 
    
    if i == len(arr):
        return
    
    helper(arr, k, i + 1, curSum + arr[i], comb + [arr[i]], result)
    helper(arr, k, i + 1, curSum, comb, result)


######################################
# Intial Wrong Approach 1 # 
######################################
def helper(arr, k, i, curSum, comb, result):
    if curSum == k and comb:
        result.append(comb)
        return 
    
    if i == len(arr):
        return
    
    helper(arr, k, i + 1, curSum + arr[i], comb + [arr[i]], result)
    helper(arr, k, i + 1, curSum, comb, result)

'''
Case: arr = [0, 0]  sum = 0   --> answer => [[0], [0], [0, 0]]

Our Answer => [[0], [0]]  
'''

######################################
# Intial Wrong Approach 2 # 
######################################
def helper(arr, k, i, curSum, comb, result):
    if curSum == k and comb:
        result.append(comb) # removed return
    
    if i == len(arr):
        return
    
    helper(arr, k, i + 1, curSum + arr[i], comb + [arr[i]], result)
    helper(arr, k, i + 1, curSum, comb, result)

'''
Case: arr = [0, 0]  sum = 0   --> answer => [[0], [0], [0, 0]]

Our Answer => [[0], [0], [0], [0, 0]]

so where are we getting the extra '0' from. Lets draw recursion tree to find out

                [0, 0]

         []               [0]

    []     [0]       [0]       [0, 0]

We can clearly see there is three '0' coming in recursion tree.
'''