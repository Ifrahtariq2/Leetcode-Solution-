class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1],[1,1]]
        if numRows == 1:
            return [ans[0]]
        elif numRows == 2:
            return ans
        else:
            for i in range(1,numRows-1):
                arr = [1]
                for j in range(len(ans[-1])-1):
                    arr.append(ans[i][j]+ans[i][j+1])
                    
                arr.append(1)
                ans.append(arr)
        return ans
        