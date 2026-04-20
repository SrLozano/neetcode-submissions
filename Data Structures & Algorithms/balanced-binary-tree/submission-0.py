# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True

        def dfs_height(node, cur_level):
            
            if not node:
                return cur_level

            return max(dfs_height(node.left, cur_level+1), dfs_height(node.right, cur_level+1))

            
        
        return (abs(dfs_height(root.left, 0) - dfs_height(root.right, 0))) <= 1