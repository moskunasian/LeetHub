class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # can have array that represents min amount possible per each idx
        # each idx will rep the min coins needed for that given amount
        # each subsequent idx is min between (curramount, min it took w.o curr coin + 1)
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if coin <= amount:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        if dp[amount] == amount + 1:
            return -1
        return dp[amount]
        