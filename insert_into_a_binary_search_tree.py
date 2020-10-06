# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        
        value = TreeNode(val)
        
        if not root:
            return value
        
        curr=root
        
        while True:
            
            if curr.val>val:
                if not curr.left:
                    curr.left = value
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = value
                    break
                else:
                    curr = curr.right
                    
        return root
                    
        
