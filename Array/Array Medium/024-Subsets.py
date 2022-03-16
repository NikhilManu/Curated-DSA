# Time O(N * 2^N) | Space O(N)

def subsets(nums):
    powerSet = []
    for i in range(len(nums) + 1):
        getPowerSet(nums, 0, i, [], powerSet)
    return powerSet

def getPowerSet(nums, idx, k, cur, powerSet):
    if len(cur) == k:
        powerSet.append(cur)
        return
    
    if idx == len(nums):
        return
    
    getPowerSet(nums, idx + 1, k, cur + [nums[idx]], powerSet) # Take 
    getPowerSet(nums, idx + 1, k, cur, powerSet)    # skip


# Solution - 2 --> DP or BFS
# Time O(N *2^N) | Space O(1)

def subsets(nums):
    powerSet = [[]]
    for num in nums:
        for i in range(len(powerSet)):
            powerSet.append(powerSet[i] + [num])
    return powerSet

def subsets(nums):
    powerSet = [[]]
    for num in nums:
        powerSet += [res + [num] for res in powerSet]
    return powerSet