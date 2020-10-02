# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        # res, stack = [], []
        # cur = root
        # while cur or stack:
        #   while cur: # travel to each node's left child, till reach the left leaf
        #     stack.append(cur)
        #     cur = cur.left
        #   cur = stack.pop() # this node has no left child
        #   res.append(cur.val) # so let's append the node value 
        #   cur = cur.right # visit its right child --> if it has left child ? append left and left.val, otherwise append node.val, then visit right child again... cur = node.right
        # return res
        
        output= []
        self.dfs(output,root)
        return output
    
    def dfs (self,output,root):
        if root:
            self.dfs(output,root.left)
            output.append(root.val)
            self.dfs(output,root.right)
        
