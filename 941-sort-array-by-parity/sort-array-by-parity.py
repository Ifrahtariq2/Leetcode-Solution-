class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        lf = 0
        for rt in range(len(nums)):
            if nums[rt] % 2 == 0:
                nums[lf] , nums[rt] = nums[rt] , nums[lf]
                lf += 1
        return nums       

        