class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def dfs(idx, result, path, nums):
            result.append(list(path))
            for i in range(idx, len(nums)):
                path.append(nums[i])
                dfs(i+1, result, path, nums)
                path.pop()
        
        result, path = [], []
        dfs(0, result, path, nums)
        return result
        
        