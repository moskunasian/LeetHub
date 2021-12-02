class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # basically, hold summations of max money robbable 
        # and i'th idx max will be either the prev houses summation, 
        # or the curr houses value + max summation from two houses ago
        
        # edge case for 2 houses or less
        if len(nums) <= 2:
            return max(nums)
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return max(dp)
        