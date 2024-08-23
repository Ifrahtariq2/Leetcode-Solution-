class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
  
        n = len(nums)
        result = [-1] * n
        stack = []
        
        for i in range(2 * n):  # Traverse twice
            current_index = i % n
            while stack and nums[stack[-1]] < nums[current_index]:
                result[stack.pop()] = nums[current_index]
            if i < n:  # Only push index on first pass
                stack.append(current_index)
        
        return result

        