# O(n) Time | O(n) Space

def TwoSum(nums, target):
    dic = {}
    for idx, first in enumerate(nums):
        second = target - first
        if second in dic:
            return [dic[second], idx]
        dic[first] = idx
    return -1