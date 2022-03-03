# Time O(N) | Space O(1)

def Container(height):
    left, right = 0, len(height) - 1
    area = 0
    while left < right:
        leftPole, rightPole = height[left], height[right]
        PoleHeight = min(leftPole, rightPole) 
        distanceBetweenPole = right - left
        
        area = max(area, PoleHeight * distanceBetweenPole)
        if leftPole > rightPole:
            right -= 1
        else:
            left += 1
        
    return area