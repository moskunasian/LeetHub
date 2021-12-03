class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # iterate over every grid pt, count and island when we first hit one
        # then, DFS to find all portions of island connected to it and change them to 'water'
        # so we will only count each island the first time we see it, giving the answer
        
        def dfs(row, col):
            # base case return when out-of-bounds or hit water
            if (row < 0 or row > len(grid)-1) or (col < 0 or col > len(grid[0])-1) or (grid[row][col] == '0'):
                return
            
            grid[row][col] = '0'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    ans += 1
        return ans
    