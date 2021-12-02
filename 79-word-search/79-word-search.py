class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def dfs(board, row, col, currWord):
            
            # no letters left to check for, mean word was found
            if len(currWord) == 0:
                return True
            
            if (row < 0 or row >= len(board)) or (col < 0 or col >= len(board[0])) or (currWord[0] != board[row][col]):
                return False
            
            # adjust what word currently is
            # also avoid using this value again for later DFS
            tmp = board[row][col]
            board[row][col] = '0'
            
            res = dfs(board, row-1, col, currWord[1:]) or \
            dfs(board, row+1, col, currWord[1:]) or \
            dfs(board, row, col-1, currWord[1:]) or \
            dfs(board, row, col+1, currWord[1:])
            
            # reinstate that value null'd from above for other searches
            board[row][col] = tmp
            
            return res
        
        # dfs check every letter to see if word exists
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, i, j, word):
                    return True
        return False
                    
        