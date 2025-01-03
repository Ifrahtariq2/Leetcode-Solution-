class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        res =0
        tsum = sum(nums)
        pres = 0
        for i in range(len(nums)-1):
            pres += nums[i]
            if pres >= (tsum - pres):
                res += 1
        return res