class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # keep matrix of previously seen max length values
        # general logic is:
        # if not equal, retrieve max from either of the previous words for curr cell
        # if equal, add one to the previous diagonal to current cell

        dp = [[0] * len(text2) for i in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[-1][-1]
                    