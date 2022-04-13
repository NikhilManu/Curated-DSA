# Time O(N^2) | Space O(1)

def longestPalindrome(s):
    longest = [0, 0]
    for i in range(len(s)):
        # here we are considering the cur index as the center of possible longest palindromic Substring
        
        bound1 = expandFromCenter(s, i, i) # - - a b b a - - -  even Palindrome
        bound2 = expandFromCenter(s, i - 1, i) # - - - a b c b a - - -   odd Palindrome
        
        currentMax = max(bound1, bound2, key=lambda x: x[1] - x[0])
        longest = max(longest, currentMax, key=lambda x: x[1] - x[0])
        
    return s[longest[0]:longest[1] + 1]

def expandFromCenter(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1; right += 1
    
    return left + 1, right - 1