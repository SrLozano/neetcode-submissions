# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        elif root.right == None:
            if root.left.val < root.val:
                return self.isValidBST(root.left)
        elif root.left == None:
            if root.right.val > root.val:
                return self.isValidBST(root.right)
        elif root.left.val < root.val and root.right.val > root.val:
            return self.isValidBST(root.left) and self.isValidBST(root.right)
        else:
            return False

#assert Solution().isValidBST(root) == False