class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        #iterate through each piece of land on the grid grid[x][y] and run dfs on each keep track using a visited set

        visited = set()
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(row,col):
            #make sure we are still in bounds:
            if(row < 0 or col < 0 or row >= rows or col >= cols):
                return
            if (row,col) in visited or grid[row][col] == '0':
                return
            visited.add((row,col))
            dfs(row+1,col)
            dfs(row-1,col)
            dfs(row,col+1)
            dfs(row,col-1)
            


        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visited and grid[row][col] == '1':
                    islands += 1
                    dfs(row,col)
        return islands

