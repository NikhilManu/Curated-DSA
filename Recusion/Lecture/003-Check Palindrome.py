# Time O(N) | Space O(N)
def isPalindrome(s):
    return isPalindromeHelper(s, 0, len(s) - 1)

def isPalindromeHelper(s, l, r):
    if l >= r:
        return True
   
    return isPalindromeHelper(s, l + 1, r - 1) if s[l] == s[r] else False