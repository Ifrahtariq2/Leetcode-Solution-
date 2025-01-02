class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        rt =0
        count = 1
        while rt<len(nums)-1:
            if nums[rt]==nums[rt+1] :
                if  count < 2:
                    rt += 1
                    count += 1
                else:
                    nums.remove(nums[rt])
                    
            else:
                count =1
                rt +=1        
        return len(nums)