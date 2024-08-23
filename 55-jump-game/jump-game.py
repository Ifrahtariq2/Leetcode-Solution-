class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        
        for i in range(len(nums)):
            # If the current index is greater than the maximum reachable index, return False
            if i > max_reach:
                return False
            
            # Update the maximum reachable index
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach or exceed the last index, return True
            if max_reach >= len(nums) - 1:
                return True
        
        return True

        