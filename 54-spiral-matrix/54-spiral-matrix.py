class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        
        rowMin, colMin = 0, 0
        rowMax, colMax = len(matrix)-1, len(matrix[0])-1
        res = []
        
        while colMin <= colMax and rowMin <= rowMax:
            
            # appending where top row is, then adjust
            for i in range(colMin, colMax+1):
                res.append(matrix[rowMin][i])
            rowMin += 1
            
            # appending where right-most col is, then adjust
            for i in range(rowMin, rowMax+1):
                res.append(matrix[i][colMax])
            colMax -= 1
            
            # append bottom going back when applicable
            if rowMin <= rowMax:
                for i in range(colMax, colMin-1, -1):
                    res.append(matrix[rowMax][i])
                rowMax -= 1
                
            # append left going up when applicable
            if colMin <= colMax:
                for i in range(rowMax, rowMin-1, -1):
                    res.append(matrix[i][colMin])
                colMin += 1
        return res
            