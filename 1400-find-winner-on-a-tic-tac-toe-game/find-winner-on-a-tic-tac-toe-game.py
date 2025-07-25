class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = []
        for i in range(3):
            grid.append([""]*3)
        
        for i, (row, col) in enumerate(moves):
            if i % 2 == 0:
                player = 'A'
            else:
                player = 'B'
            if player == 'A':
                mark = 'X'
            else:
                mark = 'O'
            grid[row][col] = mark
            
            # Check if the current player won
            # Check rows
            if grid[row][0] == grid[row][1] == grid[row][2] == mark:
                return player
            # Check columns
            if grid[0][col] == grid[1][col] == grid[2][col] == mark:
                return player
            # Check diagonals
            if (row == col) and (grid[0][0] == grid[1][1] == grid[2][2] == mark):
                return player
                #check anti-diagnol
            if (row + col == 2) and (grid[0][2] == grid[1][1] == grid[2][0] == mark):
                return player
        if len(moves) == 9:
            return "Draw" 
        else:
            return "Pending"
        