class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        longestSub = ""
        for char in s:
            if char not in longestSub:
                longestSub += char
            else:
                while char in longestSub:
                    longestSub = longestSub[1:]
                longestSub += char
            if len(longestSub) > longest:
                longest = len(longestSub)
        return longest
        