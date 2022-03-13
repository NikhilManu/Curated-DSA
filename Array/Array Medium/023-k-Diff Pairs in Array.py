# Time O(NlogN) | O(N) - Solution 1

# Sort then use two Pointer
def findPairs(nums, k):
    nums.sort() 
    count, pairs = 0, set()
    left, right = 0, 1
    while right < len(nums):
        diff = abs(nums[left] - nums[right])
        
        if left == right:
            right += 1
        elif diff == k:
            if (nums[left], nums[right]) not in pairs:
                pairs.add((nums[left], nums[right]))
                count += 1
            right += 1
        elif diff < k:
            right += 1
        else:
            left += 1
    
    return count

# Solution 1 can be improved by using binary Search
# Time O(NlogN) | Space O(N)
def findPairs(nums, k):
    nums.sort() 
    pairs = set()
    for i in range(len(nums) - 1):
        if binarySearch(nums, i + 1, nums[i] + k):
            pairs.add(nums[i])
    return len(pairs)

def binarySearch(nums, left, target):
    right = len(nums) - 1
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False

# Solution 3
# Time O(N) | Space O(N)

def findPairs(nums, k):
    unique = {}
    for num in nums:
        if num not in unique:
            unique[num] = 0
        unique[num] += 1
        
    pairs = 0
    for num in unique:
        # k == 0 means we want frequency of the cur number > 1
        if (k > 0 and num + k in unique) or (k == 0 and unique[num] > 1):
            pairs += 1
            
    return pairs