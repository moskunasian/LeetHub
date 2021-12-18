class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        shipCount = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'X':
                    shipCount += 1
                    if (i > 0 and board[i-1][j] == 'X') or (j > 0 and board[i][j-1] == 'X'):
                        shipCount -= 1
        return shipCount
    