# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        depth = 0
        level = [root] if root else []

        while level:
            depth += 1
            queue = []
            for node in level:
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
            level = queue
        return depth
