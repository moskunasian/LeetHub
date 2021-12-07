class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        rows, cols = len(matrix), len(matrix[0])
        minVal, maxVal = matrix[0][0], matrix[-1][-1]
        
        def matrixCount(num):
            count = 0
            row, col = 0, cols - 1
            while row < rows and col >= 0:
                if matrix[row][col] <= num:
                    count += col+1
                    row += 1
                else:
                    col -= 1
            return count
        
        while minVal < maxVal:
            mid = (minVal + maxVal) // 2
            count = matrixCount(mid)
            if count < k:
                minVal = mid + 1
            else:
                maxVal = mid
        return minVal
    