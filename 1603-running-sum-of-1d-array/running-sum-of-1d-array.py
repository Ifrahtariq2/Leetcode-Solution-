class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        currsm = 0
        for i in nums:
            currsm += i
            ans.append(currsm)
        return ans


        