# Time O(N) | Space O(1)

def canJump(nums):
    destination = len(nums) - 1
    for i in reversed(range(len(nums) - 1)):
        if i + nums[i] >= destination:
            destination = i

    return destination == 0;


"""
Took some Time to identify this since I was going in direction of DP and backtracking.

Intution:
    => Iterate from second Last Index
    => Try if we can jump to current Index we are standing, if we can then that index becomes the current destionation
    => if destination == 0 means we can jump
"""