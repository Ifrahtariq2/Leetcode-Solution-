class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        array = []
        currsum = 0 
        for i in nums:
            currsum += i
            array.append(currsum)
        return  array    