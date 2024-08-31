class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        lf = 0
        rt = len(arr)-1
        peak = 0
        while lf <= rt:
            mid = (lf+rt) // 2
            if arr[peak] < arr[mid]:
                peak = mid
            if arr[mid] > arr[mid +1] and mid < len(arr) -1:
                rt = mid -1
            elif arr[mid] < arr[mid +1] and mid < len(arr) -1:
                lf = mid + 1
        return peak                                                    
        