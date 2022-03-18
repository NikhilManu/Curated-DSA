# Time O(N) | Space O(k)

def subArrayDivByK(nums, k):
    dic = {0:1}
    prefixSum, count = 0, 0
    for num in nums:
        prefixSum += num
        
        if prefixSum % k in dic:
            count += dic[prefixSum % k]
            dic[prefixSum % k] += 1
        else:
            dic[prefixSum % k] = 1
    
    return count


"""
PreRequisite: Subarray Sum Equals to K
Was trying to do the same way as Subarray Sum Equals to K, where we store prefixSum in dictionary and try to check if prefixSum % k was in the dictionary. 
But this is not the right approach

How I learned this solution:
we should store (prefixSum % k) in dictionary instead of prefixSum, Now you may think why the hell should I store (prefixSUm % k) in dictionary

Explanation:
    => sum(i, j) = a[i] + a[i + 1] + .... + a[j - 1]
    => sum(i, j) = sum(0, j) - sum(0, i)

    Qn ask us to find subarray Sum divisble by k
    => sum(i , j) % k == 0

    => (sum(0, j) - sum(0, i)) % k == 0

    => (sum(0, j) % k) - (sum(0, i) % k) == 0

    Therefore, sum(0, j) % k == sum(0, i) % k

So if we find prefixSum(i) % k == prefixSum(j) % k, then it means that there exist a subarray where, sum(i , j) % k == 0
This is why we are storing PrefixSum % k in dictionary
"""