class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        arr = sorted (boxTypes, key = lambda x : x[1], reverse = True )
        print(arr)
        ans = 0
        
        for n, u in arr:
            
            if n < truckSize:
                ans += (n*u)
                truckSize -= n

            else:
                ans += (truckSize*u)
                break
        return ans

        

            