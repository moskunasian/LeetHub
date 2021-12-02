class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # idea is to init summation list each w/ smallest increasing (i.e. len: 1)
        # check all number before curr idx to see if smaller than current
        # if smaller, take max between curr idx longest or prev longest +1
        
        dp = [1 for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
        