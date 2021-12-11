class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        # very similar in logic to the robot pathing question, etc.
        # if we are ever at the first column or row, always have to just take from up or left
        # if we are outside those bounds above, take min(curr + up, curr + left)
        # RT: O(mn), Space: O(1)
        
        # resulting grid from that logic on ex given 
        # [1, 4, 5]
        # [2, 7, 6]
        # [6, 8, 7]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # @ first row
                if i == 0 and j > 0:
                    grid[i][j] = grid[i][j] + grid[i][j-1]
                # @ first col
                elif i > 0 and j == 0:
                    grid[i][j] = grid[i][j] + grid[i-1][j]
                # @ anywhere else
                elif i > 0 and j > 0:
                    takeUp = grid[i][j] + grid[i-1][j]
                    takeLeft = grid[i][j] + grid[i][j-1]
                    grid[i][j] = min(takeUp, takeLeft)
        return grid[-1][-1]
        