# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode | None) -> list[list[int]]:
        def levelorder(root):
            if not root:return []
            res = []
            q = [root]
            while q:
                vals = []
                nex = []
                for node in q:
                    vals.append(node.val)
                    if node.left:
                        nex.append(node.left)
                    if node.right:
                        nex.append(node.right)
                res.append(vals)
                q = nex 
            return res 
        return levelorder(root)[::-1]
