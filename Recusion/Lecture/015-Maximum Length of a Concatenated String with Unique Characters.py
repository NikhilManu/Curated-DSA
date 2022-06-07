# Time O() | Space O()
def stringConcatenation(arr):
    return helper(0, arr, 0, set())

def helper(i, arr, length, seen):
    if i == len(arr):
        return length
    
    if duplicateCharacterExist(seen, arr[i]):
        return helper(i + 1, arr, length, seen)
    else:
        addOrRemoveCharacter(seen, arr[i], True)
        take = helper(i + 1, arr, length + len(arr[i]), seen)
        
        addOrRemoveCharacter(seen, arr[i], False)
        skip = helper(i + 1, arr, length, seen)
        
        return max(take, skip)
          
def duplicateCharacterExist(visitedCharacters, string):
    currentStringCharacters = set()
    for char in string:
        if char in visitedCharacters:
            return True
        
        if char in currentStringCharacters:
            return True
        currentStringCharacters.add(char)
        
    return False

def addOrRemoveCharacter(seen, string, add):
    for char in string:
        if add:
            seen.add(char)
        else:
            seen.remove(char)

