# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.ans = []
        def dfs(node, path, summ):
            if not node:
                return []
            summ += node.val
            path.append(node.val)
            if not node.left and not node.right  and summ == targetSum:
                self.ans.append(path.copy())
            if node.left:
                dfs(node.left, path, summ)
            if node.right:
                dfs(node.right, path, summ)   
            path.pop()
        dfs(root,[],0)
        return self.ans