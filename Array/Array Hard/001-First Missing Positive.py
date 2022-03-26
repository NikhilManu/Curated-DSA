# Time O(N) | Space O(1)

def firstMissingPositive(nums):
    removeNegativeNumbers(nums)
    markVisitedNumbers(nums)
            
    for i, num in enumerate(nums):
        if num > 0:
            return i + 1
        
    return len(nums) + 1
    
def removeNegativeNumbers(nums):
    for i, num in enumerate(nums):
        if num <= 0:
            nums[i] = float('inf')
        
def markVisitedNumbers(nums):
    for num in nums:
        index = abs(num) - 1
        if index < len(nums):
            nums[index] = -abs(nums[index])


"""
Intution: 
    The Possible answers are only in range (1, n + 1) where n -> length of the array

    => So firstly we dont care about the negative numbers, so we remove them
    => Then, we are making index to negative if we visit any number. (if we get a number 3, then we will make index 2 to negative)
    => Now iterate throught the array and find the first index with positive number
"""

# Time O(N) | Space O(1)

# Do a cyclic sort and check if every index have value index + 1