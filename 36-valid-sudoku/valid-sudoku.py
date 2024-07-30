class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                value = board[r][c]
                
                # Check if value is in any of the sets
                if value in row[r] or value in col[c] or value in squares[r // 3 * 3 + c // 3]:
                    return False
                
                # Add value to the appropriate sets
                row[r].add(value)
                col[c].add(value)
                squares[r // 3 * 3 + c // 3].add(value)

        return True
