class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        output = []
        for c in range(cols) :
            row = []
            for r in range(rows):
                row.append(matrix[r][c])
            output.append(row)        
        
        return output
        