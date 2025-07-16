class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
    
        for num in nums:
            # Compare based on absolute value first
            if abs(num) < abs(closest):
                closest = num
            elif abs(num) == abs(closest):
                # If tie, choose the larger value
                closest = max(closest, num)
        return closest

        