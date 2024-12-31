class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lf = 0
        res =0
        zero =  0
        for rt in range(len(nums)):
            if nums[rt] == 0:
                zero += 1
            while zero > k:
                if nums[lf] ==0:
                    zero -= 1
                lf += 1

            res = max(res, rt - lf + 1)
            
        return res

        