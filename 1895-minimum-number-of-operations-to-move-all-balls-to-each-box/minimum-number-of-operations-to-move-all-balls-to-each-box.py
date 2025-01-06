class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        opr = []
        n = len(boxes)
        lf = 0
        while lf < n: 
            count = 0
            for i in range(0,n): 
                if boxes[i] =="0":
                    continue
                if   boxes [i] == "1":
                    count += abs(i - lf)
            opr.append(count)  
            lf += 1      
        return opr