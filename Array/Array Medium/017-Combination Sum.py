# if no duplicates were allowed then Time would be O(2 ^ N)

# Time O(k * 2 ^ N) | Space O(N)
def CombinationSum(nums, target):
    result = []
    getAllCombination(nums, 0, target, [], result)
    return result

def getAllCombination(nums, idx, target, comb, result):
    if target == 0:
        result.append(comb)
        return
    
    if target < 0:
        return

    for i in range(idx, len(nums)):
        getAllCombination(nums, i, target - nums[i], comb + [nums[i]], result)
        
def getAllCombination(nums, idx, target, comb, result):
    if target == 0:
        result.append(comb)
        return
    
    if idx == len(nums) or target < 0:
        return

    # skip the current element
    getAllCombination(nums, idx + 1, target, comb, result)

    # take the current element
    getAllCombination(nums, idx, target - nums[idx], comb + [nums[idx]], result)
    # we are only passing comb + [nums[idx]] into the function so comb at the current level is never changing
    # if we are using comb.append(nums[i]) the after the recursive call you have to pop the element

