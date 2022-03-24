# Time O(N) | Space O(N)

def findMaxValueOfEquation(points, k):
    res = float('-inf')
    queue = deque([])
    for xj, yj in points:
        while queue and xj - queue[0][0] > k:
            queue.popleft()
            
        if queue:
            res = max(res, yj + xj + queue[0][1])
            
        while queue and queue[-1][1] <= yj - xj:
            queue.pop()
            
        queue.append((xj, yj - xj))
        
    return res

"""
ans = maximum (yi + yj + |xi - xj|)
    since xi < xj for i < j as array is sorted by x
    ans = maximum (yi + yj + xj - xi)
    ans = maximum (xj + yj + (yi - xi))

    So what we are trying to do is finding max(yi - xi)
"""