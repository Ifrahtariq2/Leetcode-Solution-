class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        freq = 0
        val =  1
        res  = [] 
        while val<len(nums) :
            res += ([nums[val]] * nums[freq] )
            freq += 2
            val += 2

        return res
            

        