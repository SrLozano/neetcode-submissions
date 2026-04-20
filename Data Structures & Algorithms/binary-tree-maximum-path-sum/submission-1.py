# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        cur_max = -math.inf

        def dfs(node):
            if not node:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
        
            nonlocal cur_max
            cur_max = max(cur_max, left + right + node.val)

            return node.val + max(left, right)

        return max(dfs(root), cur_max)
