class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        
        # dfs for every letter in grid
        # return false if OOB or not desired letter
        # return true if no letters left to check for 
        # dfs will return OR for each direction
        # side pt: have to null out where we've searched before each dfs
        
        def dfs(i, j, word):
            
            if len(word) == 0:
                return True
            
            if (i < 0 or i >= len(board)) or (j < 0 or j >= len(board[0])) or (word[0] != board[i][j]):
                return False
            
            tmp = board[i][j]
            board[i][j] = 0
            res = dfs(i-1, j, word[1:]) or dfs(i+1, j, word[1:]) or dfs(i, j-1, word[1:]) or dfs(i, j+1, word[1:])
            board[i][j] = tmp
            return res
        
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, word):
                    return True
                    
        