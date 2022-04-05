# Time O(N) | Space O(1)

def validPalindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return isPalindrome(string[left + 1: right + 1]) or isPalindrome(string[left:right])
        
        left += 1; right -= 1
        
    return True

def isPalindrome(string):
    left, right = 0, len(string) - 1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1; right -= 1
        
    return True


"""
Intution:

    => a b c c b x a  (elimination last and first element since they are same)

    => b c c b x  ( Here we have to try deleting the first and last letter.)

    => ( b c c b ) or ( c c b x ) if any is palindrome then, answer is true 
"""
            