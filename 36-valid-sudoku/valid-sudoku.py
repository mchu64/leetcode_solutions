class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                value = board[r][c]
                
                if value in row[r] or value in col[c] or value in squares[(r // 3,c // 3)]:
                    return False
                
                row[r].add(value)
                col[c].add(value)
                squares[(r // 3,c // 3)].add(value)

        return True
