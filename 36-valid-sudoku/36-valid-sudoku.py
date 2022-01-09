class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # seen = []
        # for i, row in enumerate(board):
        #     for j, c in enumerate(row):
        #         if c != '.':
        #             seen += [(c,j),(i,c),(i//3,j//3,c)]
        # return len(seen) == len(set(seen))
        
        return self.isRowValid(board) and self.isColValid(board) and self.isCubeValid(board)
        
    def isUnitValid(self, unit):
        unit = [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    def isRowValid(self, board):
        for row in board:
            if not self.isUnitValid(row):
                return 0
        return 1
                
    def isColValid(self, board):
        for col in zip(*board):
            if not self.isUnitValid(col):
                return 0
        return 1
    
    def isCubeValid(self, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                cube = [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                if not self.isUnitValid(cube):
                    return 0
        return 1
    