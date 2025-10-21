class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = set()

        def dfs(row,col,index):

            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            if (row, col) in visited:
                return False
            if index == len(word) - 1 and board[row][col] == word[index]:
                return True
            if board[row][col] == word[index]:
                visited.add((row,col))
                found = dfs(row+1,col, index+1) or dfs(row-1,col, index+1) or dfs(row,col+1, index+1) or dfs(row,col-1, index+1)
                visited.remove((row,col))
                return found


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and dfs(row,col,0):
                    return True

        return False