# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def helper(lfsubtree,rtsubtree):
            if lfsubtree == None and rtsubtree == None:
                return True
            if lfsubtree == None or rtsubtree == None:
                return False
            if lfsubtree.val != rtsubtree.val :
                return False
            
            return helper(lfsubtree.left,rtsubtree.right) and helper(lfsubtree.right,rtsubtree.left)
        return helper(root.left,root.right)

        