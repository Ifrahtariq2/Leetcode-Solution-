class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        lf = 0
        rt = len(nums ) -1
        while lf <= rt:
            mid = (lf + rt) // 2
            if nums[mid] == target:
                return mid
            if nums[lf] <= nums[mid]:
                if nums[lf] <= target < nums[mid]:
                    rt = mid - 1
                else:
                    lf = mid + 1
            else:
                if nums[mid] < target <= nums[rt]:
                    lf = mid + 1
                else:
                    rt = mid -1                
        return -1
        