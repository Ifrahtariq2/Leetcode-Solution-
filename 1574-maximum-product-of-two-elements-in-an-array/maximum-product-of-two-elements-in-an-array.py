class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        greatest = max(nums)
        nums.remove(greatest)
        greater2 = max(nums)
        product = (greatest-1)* (greater2 - 1)
        return product