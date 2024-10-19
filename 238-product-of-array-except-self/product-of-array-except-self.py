class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        array = [1] * n  # Step 1: Initialize output array with 1s

        # Step 2: First pass - calculate left products
        left_product = 1
        for i in range(n):
            array[i] = left_product
            left_product *= nums[i]

        # Step 3: Second pass - calculate right products
        right_product = 1
        for i in range(n - 1, -1, -1):
            array[i] *= right_product
            right_product *= nums[i]

        return array
        
        