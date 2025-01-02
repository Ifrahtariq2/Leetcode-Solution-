class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        # lf , rt, prev = 0,1,""
        # maxl=1
        # while rt < len(arr):
        #     if arr[rt-1] < arr[rt] and prev != "<":
        #         maxl = max(maxl,rt -lf + 1)
        #         rt += 1
        #         prev = "<"
        #     elif arr[rt-1]> arr[rt] and prev != ">":
        #         maxl = max(maxl,rt -lf + 1)
        #         rt += 1
        #         prev = ">"
        #     else:
        #         if arr[rt-1] == arr[rt] :
        #             lf = rt
        #         else:
        #             lf = rt-1
        #         rt += 1 
        #         prev = ""
        # return maxl
        if len(arr) == 1:
            return 1
        start = 0
        maxl = 1
        for i in range(1,len(arr)):
            if i == len(arr)-1 or not (arr[i-1] < arr[i] > arr[i+1] or arr[i-1] > arr[i] < arr[i+1]):
                if arr[i] != arr[i-1]:
                    maxl = max (maxl, i-start+1)
                start = i
        return maxl



        