# Time (lines * maxWidth) | Space O(lines * maxWidth)

#https://www.youtube.com/watch?v=GqXlEbFVTXY
def textJustification(words, maxWidth):
    result = []
    i, n = 0, len(words)
    while i < n:
        j = i + 1
        lineLength = len(words[i])
        while j < n and lineLength + len(words[j]) + (j - i - 1) < maxWidth: # (j - i) gives the number of words, (j - i - 1) gives the space
            lineLength += len(words[j])
            j += 1
            
        remainingSpace = maxWidth - lineLength
        numberOfWords = j - i
        if numberOfWords == 1 or j >= n:
            result.append(leftJustify(words, remainingSpace, i, j))
        else:
            result.append(middleJustify(words, remainingSpace, i, j))
            
        i = j
        
    return result
    
def middleJustify(words, remainingSpace, i, j):
    spacesNeeded = j - i - 1
    spaces = remainingSpace // spacesNeeded
    extraSpaces = remainingSpace % spacesNeeded
    
    res = words[i]
    for k in range(i + 1, j):
        spacesToApply = spaces + ( 1 if extraSpaces > 0 else 0 )
        extraSpaces -= 1

        res += ' ' * spacesToApply + words[k]
        
    return res
        
def leftJustify(words, remainingSpace, i, j):
    spacesOnRight = remainingSpace - (j - i - 1) # we have to subtract common space from remainingSpace, so we can add extra to RightSide
    
    res = words[i]
    for k in range(i + 1, j):
        res += ' ' + words[k]
        
    res += ' ' * spacesOnRight
    return res