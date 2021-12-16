class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # using bastard-child kadanes algo logic
        # take the min of the last two step to current
        # then, take the min of the last two summated values will answer
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
        