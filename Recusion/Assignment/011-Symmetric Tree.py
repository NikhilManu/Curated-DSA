# Time O(N) | Space O(N)

def isSymmetric(root):
    return helper(root, root)

def helper(rootA, rootB):
    if not rootA and not rootB:
        return True
    
    if not rootA or not rootB:
        return False
    
    if rootA.data != rootB.data:
        return False
    
    return helper(rootA.left, rootB.right) and helper(rootA.right, rootB.left)