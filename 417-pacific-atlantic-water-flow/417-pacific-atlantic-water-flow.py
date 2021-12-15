class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m, n = len(heights), len(heights[0])
        atlSeen = set()
        pacSeen = set()
        
        # idea is to dfs starting from both pacific & atlantic sides
        # keep dfs going until out of bounds or water attempting to flow 'up'
        
        def dfs(seenSet, row, col, currHeight):
            # break dfs if: out-of-bounds, prev height larger, already seen this cell
            if (row < 0 or row >= m) or (col < 0 or col >= n) or  (row, col) in seenSet or (currHeight > heights[row][col]):
                return
            
            seenSet.add((row, col))
            currHeight = heights[row][col]
            dfs(seenSet, row-1, col, currHeight)
            dfs(seenSet, row+1, col, currHeight)
            dfs(seenSet, row, col-1, currHeight)
            dfs(seenSet, row, col+1, currHeight)    
            
        
        # iterate over cols starting from both pac/atl sides
        for col in range(n):
            dfs(pacSeen, 0, col, heights[0][col])
            dfs(atlSeen, m-1, col, heights[m-1][col])
        
        # iterate over rows starting from both pac/atl sides
        for row in range(m):
            dfs(pacSeen, row, 0, heights[row][0])
            dfs(atlSeen, row, n-1, heights[row][n-1])
            
        return list(atlSeen.intersection(pacSeen))
    