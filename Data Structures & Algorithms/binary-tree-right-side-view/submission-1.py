# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        right_view = {}

        def dfs(node, level):
            if node:
                if level not in right_view.keys():
                    right_view[level] = node.val

                if node.right:
                    dfs(node.right, level+1)
                if node.left:
                    dfs(node.left, level+1)

        dfs(root, 0)
        return list(right_view.values())