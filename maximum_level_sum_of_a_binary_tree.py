# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        if not root.right and not root.left:
            return root.val
        
        level=0
        max_level=0
        max_sum=(float('-inf'))
        queue = collections.deque()
        queue.append(root)
        
        while queue:
            level+=1
            temp_sum=0
            for i in range (len(queue)):
                node=queue.popleft()
                temp_sum+=node.val
                
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            if temp_sum> max_sum:
                max_sum=temp_sum
                max_level=level
        return max_level
            
