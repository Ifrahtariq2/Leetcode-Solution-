# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None 
        rootval = preorder[0]
        rootidx = inorder.index(rootval)
        root = TreeNode(rootval)
        root.left= self.buildTree(preorder[1 : rootidx + 1 ], inorder[:rootidx])
        root.right= self.buildTree(preorder[rootidx+1:], inorder[rootidx+1: ])

        return root
        