# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if not q and not p:
            return True
        
        if not q and p:
            return False
        
        if q and not p:
            return False
        
        return q.val==p.val and self.isSameTree(p.right,q.right) and self.isSameTree(p.left,q.left)
