class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        hm = {}
        for i in range(len(nums)):
            if ( target - nums[i]  ) not in hm:
                hm[nums[i]] = i
            else:
                ans.append(i)
                ans.append(hm[target - nums[i]])

        return ans
        