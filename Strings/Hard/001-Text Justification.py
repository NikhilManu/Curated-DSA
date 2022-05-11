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
    spaceAfterWords = remainingSpace // spacesNeeded
    extraSpaces = remainingSpace % spacesNeeded
    
    res = []
    for idx in range(i, j):
        spacesToApply = spaceAfterWords + ( 1 if extraSpaces > 0 else 0 )
        extraSpaces -= 1
        
        res.append(words[idx])
        res.append('' if idx == j - 1 else ' ' * spacesToApply)
        
    return ''.join(res)
        
def leftJustify(words, remainingSpace, i, j):
    spacesOnRight = remainingSpace - (j - i - 1) # we have to subtract common space from remainingSpace, so we can add extra to RightSide
    
    res = []
    for idx in range(i, j):
        res.append(words[idx] if idx == j - 1 else words[idx] + ' ')
        
    res.append(' ' * spacesOnRight)
    return ''.join(res)