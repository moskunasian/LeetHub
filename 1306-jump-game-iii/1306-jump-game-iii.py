class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        # bastardized version of DFS
        # if we are out of bounds return false
        # else check to left and right
        # same idea as sinking islands where we remove visited for current recurse
        
        left, right = 0, len(arr)
        def dfs(i):
            
            
            if (i < left or i >= right or arr[i] < 0):
                return False
            
            if arr[i] == 0:
                return True
            
            arr[i] = -arr[i]
            poss1 = dfs(i - arr[i]) 
            poss2 = dfs(i + arr[i])
            arr[i] = -arr[i]
            
            return poss1 or poss2
            
        return dfs(start)
    