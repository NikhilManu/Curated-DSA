# Time O(N) | Space O(N)

def lengthOfSubstring(string):
    left, right, longest = 0, 0, 0
    used = set()
    while right < len(string):
        if s[right] in used:
            used.remove(string[left])
            left += 1
        else:
            used.add(string[right])
            longest = max(longest, right - left + 1)
            right += 1
            
    return longest