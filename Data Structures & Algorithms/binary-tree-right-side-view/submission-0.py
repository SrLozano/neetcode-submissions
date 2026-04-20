# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        right_view = []

        def dfs(node):
            if node:
                right_view.append(node.val)

                if node.right:
                    dfs(node.right)
                elif node.left:
                    dfs(node.left)

        dfs(root)
        return right_view