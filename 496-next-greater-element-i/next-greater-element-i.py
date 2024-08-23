class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = {n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        arr = []         
        for i in range(len(nums2)):
            while arr and nums2[i] > arr[-1]:
                idx = nums1Idx[arr.pop()]
                res[idx] = nums2[i]
            if nums2[i] in nums1Idx:
                arr.append(nums2[i])
        return res
        
        