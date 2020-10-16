# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') ->'TreeNode':
        
        p_val=p.val
        q_val=q.val
        node=root
        
        while node:

            if (node.val<p_val and node.val<q_val):
                node = node.right
            if (node.val>q_val and node.val>p_val):
                node = node.left
            else:    
                return node
