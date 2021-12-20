class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        # since it's just consecutive 1's we can use kadanes algo
        
        for i in range(1, len(nums)):
            if nums[i - 1] and nums[i] == 1:
                nums[i] = nums[i - 1] + 1
                
        return max(nums)
    