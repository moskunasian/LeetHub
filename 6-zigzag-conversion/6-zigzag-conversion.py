class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # general algo:
        # if only one row can return just the string
        # keep track of current row and if we are curr going up / down
        # if we are at 0 or at bottom, we switch the direction we are going
        
        if numRows == 1:
            return s
        
        rows = ["" for _ in range(min(numRows, len(s)))]
        
        currRow = 0
        goingDown = False
        for char in s:
            
            # append char to curr row we are on
            rows[currRow] += char
                
            # check if we are going down or not
            if (currRow == 0 or currRow == len(rows) - 1): 
                goingDown = not goingDown
                
            if goingDown:
                currRow += 1
            else:
                currRow -= 1
                
        answer = ''
        for row in rows:
            answer += row
        return answer
        