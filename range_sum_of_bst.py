# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        suma = 0
        stack = [root]
        if root is None:
            return 0
        while len(stack) > 0:
            curr = stack.pop()
            if (L <= curr.val <= R):
                suma += curr.val
            if (curr.left != None):
                stack.append(curr.left)
            if (curr.right != None):
                stack.append(curr.right)

        return suma
