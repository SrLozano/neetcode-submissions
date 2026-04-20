# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(t1, t2):
            if t1 == None or t2 == None:
                if t1 == None and t2 == None:
                    return True
                else: 
                    return False

            if t1.val == t2.val and dfs(t1.left,  t2.left) and dfs(t1.right,  t2.right):
                return True

            return False

        return dfs(p, q)

        