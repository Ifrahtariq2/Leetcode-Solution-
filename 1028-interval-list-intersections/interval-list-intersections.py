class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList == [] or secondList == []:
            return []
        res = []
        i , j = 0 , 0
        while i < len(firstList) and j < len(secondList):
            lf = max(firstList[i][0], secondList[j][0])
            rt = min(firstList[i][1], secondList[j][1])
            if lf <= rt:
                res.append([lf,rt])
            if firstList[i][1] < secondList[j][1]:
                i+=1
            else:
                j+=1
        return res

        