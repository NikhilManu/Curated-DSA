# Solution 1 - Divide and Conquer
# Time O(Nlogn) | Space O(logn)
def majorityElement(nums):
    return rec(nums, 0, len(nums) - 1)

def rec(nums, low, high):
    if low == high:
        return nums[low]
    
    mid = low + (high - low) // 2
    left = rec(nums, low , mid)
    right = rec(nums, mid + 1, high)
    
    leftCount, rightCount = 0, 0
    for i in range(low, high + 1):
        if left == nums[i]:
            leftCount += 1
        if right == nums[i]:
            rightCount += 1
            
    return left if leftCount > rightCount else right


# Solution 2 - Sorting
# Time O(NlogN) | Space O(1) Assuming the sorting is inPlace
def majorityElement(nums):
    nums.sort()
    return nums[len(nums) // 2]

# Solution - boyer Moore Voting Algorithm
# Time O(N) | Space O(1)
def majorityElement(nums):
    candidate, vote = 0, 0
    for num in nums:
        if vote == 0:
            candidate = num
        
        vote += 1 if candidate == num else -1
        
    return candidate

# Find a candidate if the vote becomes zero
# if the candidate occurs again increment else decrement
# By repeating this process will ultimately lead to have the candidate which
# occurs more than half
