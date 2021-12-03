class Trie:
    def __init__(self):
        self.level = {}
        
    def insert(self, word):
        nextLevel = self.level
        for c in word:
            if c not in nextLevel:
                nextLevel[c] = {}
            nextLevel = nextLevel[c]
        nextLevel['end'] = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(row, col, level, word):
            # if we are at the end of the trie, we found the word
            if 'end' in level:
                result.add(word)
                
            # bounds for us to break: we are out of board bounds or Trie doesn't account for curr letter
            if (row < 0 or row == rowNum) or (col < 0 or col == colNum) or (board[row][col] not in level):
                return
            
            # update Trie position and what word currently is 
            level = level[board[row][col]]
            word += board[row][col]
            
            # set temp for rest of search that occurs and restore it later
            tmp = board[row][col]
            board[row][col] = '.'
            
            dfs(row-1, col, level, word)
            dfs(row+1, col, level, word)
            dfs(row, col-1, level, word)
            dfs(row, col+1, level, word)
            board[row][col] = tmp
            
            
        # actually the same solution as Word Search I
        # but now since we have to search for multiple words
        # use a trie to store them and whenever we are at the 
        # end of a tree branch we have found a word
        
        trie, result = Trie(), set()
        rowNum, colNum = len(board), len(board[0])
        for word in words:
            trie.insert(word)
            
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, trie.level, '')
        return list(result)
                