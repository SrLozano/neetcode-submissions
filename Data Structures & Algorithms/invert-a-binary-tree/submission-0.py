# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root is None:
            return root 
        
        # base case just val 
        if root.left is None and root.right is None:
            return root

        '''# base case just val and left
        if root.left and root.right is None:
            root.right = root.left
            root.left = None
            return root

        # base case just val and right
        if root.right and root.left is not None:
            root.left = root.right
            root.right = None
            return root'''

        root.left, root.right = root.right, root.left

        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        return root