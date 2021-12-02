class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # same as house robber 1
        # but, we just plug in houses w/o first house,
        # then w/o the last house
        
        if len(nums) <= 2:
            return max(nums)
        
        def robbing(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            for i in range(2, len(nums)):
                # max between curr house and max prof from two houses ago
                # or just the last max profit
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            return max(dp)
        
        return max(robbing(nums[1:]), robbing(nums[:-1]))
        