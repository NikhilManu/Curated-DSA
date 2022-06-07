# Time Limit Exceeded
# Time O(2 ^(kn)) | Space O(kn)
def canPartitionKSubsets(arr, k):
    arrSum = sum(arr)
    if arrSum % k != 0:
        return False
    return helper(0, 1, 0, arrSum / k, k, arr, set())
    
def helper(i, bucketNum, bucketSum, reqSum, k, arr, seen):
    if bucketNum == k + 1:
        return True
    
    if bucketSum == reqSum:
        return helper(0, bucketNum + 1, 0, reqSum, k, arr, seen)
    
    if bucketSum > reqSum or i >= len(arr):
        return False

    if i in seen:
        return helper(i + 1, bucketNum, bucketSum, reqSum, k, arr, seen)
    else:
        seen.add(i)
        picked = helper(i + 1, bucketNum, bucketSum + arr[i], reqSum, k, arr, seen)
        
        seen.remove(i)
        skiped = helper(i + 1, bucketNum, bucketSum, reqSum, k, arr, seen)
        
        return picked or skiped


# Dynamic Programming --