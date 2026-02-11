# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def helper(node, path,remaining):
            if node == None:
                return
            
            
            path.append(node.val)
            remaining -= node.val
            


            
            if node.left == None and node.right == None and remaining == 0:

                ans.append(path.copy()) # why path.copy?
                print(ans)
            
            helper(node.left, path,remaining)
            helper(node.right, path,remaining)
            
            path.pop() 
            print(path)
            
             
            
        helper(root , [],targetSum)
        return ans