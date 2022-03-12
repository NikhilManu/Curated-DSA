# Time O(N) | Space O(1)

def maxScore(cardPoints, k):
    if len(cardPoints) == k:
        return sum(cardPoints)
    
    n = len(cardPoints)
    left, right = k - 1, n - 1
    
    maxPoints = sum(cardPoints[i] for i in range(k))
    currentPoints = maxPoints
    while left >= 0:
        currentPoints = (currentPoints - cardPoints[left]) + cardPoints[right]
        left -= 1; right -= 1
        maxPoints = max(maxPoints, currentPoints)
        
    return maxPoints

# Same solution as above but done in reverse 
def maxScore(cardPoints, k):
    if len(cardPoints) == k:
        return sum(cardPoints)
    
    n = len(cardPoints)
    left, right = 0, n - k
    
    maxPoints = sum(cardPoints[i] for i in range(right, n))
    currentPoints = maxPoints
    while left < k:
        currentPoints = (currentPoints - cardPoints[right]) + cardPoints[left]
        maxPoints = max(maxPoints, currentPoints)
        left += 1; right += 1

    return maxPoints