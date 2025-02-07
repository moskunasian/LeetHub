class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        if len(dp) <= 2:
            return dp[-1]
        
        for i in range(2, len(dp)):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]
        