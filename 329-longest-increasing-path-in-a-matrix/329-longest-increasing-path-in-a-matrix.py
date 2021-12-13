class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        # as usual, hard problems aren't necessarily harder in a 'logic' sense
        # just normally have to use more than a single data struct
        # for this case, it's a DP matrix as well as dfs
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            # if this dp cell has already been visited previously
            # just return its calculated value
            if dp[i][j] > 0:
                return dp[i][j]
            
            currMax = 0
            for x, y in [ (i-1, j), (i+1, j), (i, j-1), (i, j+1) ]:
                # only checking next when we are inbound 
                # and the next value is an increasing one
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    currMax = max(currMax, dfs(x, y) + 1)
            dp[i][j] = currMax
            return currMax
        
        answer = 0
        for i in range(m):
            for j in range(n):
                answer = max(answer, dfs(i, j) + 1)
            
        return answer
        