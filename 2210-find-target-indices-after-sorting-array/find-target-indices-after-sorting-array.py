class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
     
        nums.sort()
        
        array = []
        
        for i in range(len(nums)):
            if nums[i] == target:
              array.append(i)
         
        return array