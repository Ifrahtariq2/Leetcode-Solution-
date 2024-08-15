class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        lf = 0
        rt = len(nums) - 1
        nums.sort()
        arr = []
        while  lf < rt:
            alice = nums[lf]
            lf += 1
            bob = nums[lf]
            lf += 1
            arr.append(bob) 
            arr.append(alice)     
        return arr    
    
        