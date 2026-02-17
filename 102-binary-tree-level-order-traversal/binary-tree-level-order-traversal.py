# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        def traverse(node, level, ans):
            if node == None:
                return
            if len(res) <= level:
                ans.append([])
            res[level].append(node.val)
            traverse(node.left, level+1, ans)
            traverse(node.right, level+1, ans)

        traverse(root, 0 ,res)
        return res
        