# Time O(N) | Space O(1)

def jumpGame(nums):
    if len(nums) == 1: return 0
    currentPosition, maxReachablePosition = 0, nums[0]
    jumps = 1
    while maxReachablePosition < len(nums) - 1:
        furthestPossibleJump = max(i + nums[i] for i in range(currentPosition, maxReachablePosition + 1))
        currentPosition, maxReachablePosition = maxReachablePosition, furthestPossibleJump
        jumps += 1
        
    return jumps


"""
if we try to just find the largest number in range (currentPosition, nums[currentPostion])
    TestCase: [10,9,8,7,6,5,4,3,2,1,1,0]
    This will fail, since from 10 it will jump to 9 and so on.
    The Answer should be 2, since from 10 it can directly jump to second lastIdx

Intution:
    We are trying to reach furthest Idx using two Jumps
    So furthestPossibleJump stores max values of currentPosition --> idx --> nums[idx]   (idx can be range(currentPosition, maxReachablePosition))
"""