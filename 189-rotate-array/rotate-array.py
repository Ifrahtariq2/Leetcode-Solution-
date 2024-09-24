class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]* len(nums)
        for i in range(len(nums)):
            index = (i + k )% len(nums)
            res[index] = nums[i]
        for i in range(len(res)):
            nums[i] = res[i]

        