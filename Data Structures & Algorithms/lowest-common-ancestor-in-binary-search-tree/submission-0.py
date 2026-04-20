# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        cur = root

        # make sure p is lowest than q
        if p.val > q.val:
            p, q = q, p

        while cur:
            print(f"cur.val: {cur.val}, p.val: {p.val}, q.val:{q.val}")
            print(f"{cur.val >= p.val and cur.val <= q.val}")
            if cur.val >= p.val and cur.val <= q.val:
                return cur
            elif cur.val > p.val and cur.val > q.val:
                cur = cur.left
            else:
                cur = cur.right

        return None