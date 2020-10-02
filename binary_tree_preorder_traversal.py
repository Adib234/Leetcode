# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # Iterative
        # stack = [root] 
        # output = []
        # while stack:
        #     node = stack.pop()
        #     if node:
        #         output.append(node.val)
        #         stack.append(node.right)
        #         stack.append(node.left)
        # return output
        #
        # Recursive
        
        output=[]
        self.dfs(output,root)
        return output
    
    def dfs(self,output,root):
        if root:
            output.append(root.val)
            self.dfs(output,root.left)
            self.dfs(output,root.right)
