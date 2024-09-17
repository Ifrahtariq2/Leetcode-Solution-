class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        maxlen = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0 and nums[i] <= threshold:
                j = i + 1
                while j < len(nums):
                    if nums[j] % 2 != nums[j - 1] % 2 and nums[j] <= threshold:
                        j += 1 
                    else:
                        break
                maxlen = max(maxlen,j - i  )
        return maxlen        