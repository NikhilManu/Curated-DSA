# Time O(N) | Space O(N)

def largestRectangle(heights):
    stack, maxArea = [], 0
    for idx, height in enumerate(heights + [0]):
        while stack and heights[stack[-1]] >= height:
            h = heights[stack.pop()]
            l = idx if not stack else idx - stack[-1] - 1 # if stack is empty then it means every height before current height is greater
            maxArea = max(maxArea, h * l)
        stack.append(idx)
    return maxArea

# Good Explanations
# https://abhinandandubey.github.io/posts/2019/12/15/Largest-Rectangle-In-Histogram.html
# https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/995249/Python-increasing-stack-explained

"""
Reason for Adding [0] to end of heights is simple

Assume Case: [2, 4, 5]
    => In this case maxArea will not be calculated, since to calculate we need to encounter a height which is less than the top of stack
    So if zero is added in heights
            heights = [2, 4, 5, 0]
     
            After stack = [2, 4, 5], then when 0 comes we pop the top of stack and do calculations for getting the area
"""
