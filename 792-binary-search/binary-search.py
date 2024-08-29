class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf = 0 
        rt = len(nums) -1
        while lf <= rt:
            mid = (lf + rt) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lf = mid + 1
            else:
                rt = mid - 1   
        return -1