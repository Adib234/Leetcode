# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
       
        self.inorder=[]
        self._inorder(root)
        self.index=-1
    def _inorder(self,root):
        if not root:
            return []
        
        self._inorder(root.left)
        self.inorder.append(root.val)
        self._inorder(root.right)
        
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index+=1
        return self.inorder[self.index]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.inorder)-2>=self.index


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
#Does not satisfy o(h) requirement
