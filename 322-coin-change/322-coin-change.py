class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # can have a state array that holds min amount for each coin amount
        # when coin is less than current amount 
        # take min of current amount and how much it took for that (last coin + 1)
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0 # always 0 for 0 amount required
        for i in range(amount + 1):
            for coin in coins:
                if coin <= amount:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # if our amount index is less than what we set above, viable min amount
        # else, no min amount possible so just return -1
        if dp[amount] < amount+1:
            return dp[amount]
        return -1
        