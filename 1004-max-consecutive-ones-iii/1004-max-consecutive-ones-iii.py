class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
                
        l, r = 0, 0
        result = 0
        seen = 0 
        
        while r < len(nums):
            if nums[r] == 0:
                seen += 1
                
                # if we have more 0's than allowed
                # constrict left side of window until valid
                while seen > k:
                    seen = seen - 1 if nums[l] == 0 else seen
                    l += 1
            result = max(result, r - l + 1)  
            r += 1
            
        return result