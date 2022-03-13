# Time (HlogH + VlogV) | Space O(1)

# Just draw the diagram and will see the logic directly
def maxArea(h, w, horizontalCuts, verticalCuts):
    horizontalCuts.sort(); verticalCuts.sort()
    
    maxHorizontalCut = max(horizontalCuts[0], h - horizontalCuts[-1])
    for i in range(1, len(horizontalCuts)):
        maxHorizontalCut = max(maxHorizontalCut, horizontalCuts[i] - horizontalCuts[i - 1])
    
    maxVerticalCut = max(verticalCuts[0], w - verticalCuts[-1])
    for i in range(1, len(verticalCuts)):
        maxVerticalCut = max(maxVerticalCut, verticalCuts[i] - verticalCuts[i - 1])
    
    return (maxHorizontalCut * maxVerticalCut) % (10**9 + 7)