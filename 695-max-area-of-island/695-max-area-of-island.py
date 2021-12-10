class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        
        # generally same idea as [ number of islands ]
        # but now we just need to count the size of the islands
        # how this will be different from [ number of islands ]:
            # when we reach base case return 0 because not on island
            # adding 1's to the recurse call stack to count valid cells per island
            # retrieving the max from each cell 
        
        def dfs(row, col):
            if (row < 0 or row >= len(grid)) or (col < 0 or col >= len(grid[0])) or (grid[row][col] == 0):
                return 0
            
            grid[row][col] = 0
            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
        
        maxArea = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row, col))
        return maxArea
    