class Solution:
    def longestPalindrome(self, s: str) -> str:
       
        # general idea is to iterate over each idx
        # bloom outward from each as long as in bounds and chars match
        # edge case is even and odd case (i.e. aba vs. abba)
        
        if len(s) == 1:
            return s
        
        def bloom(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]
        
        longest = ''
        for i in range(len(s)):
            evenCase = bloom(s, i, i+1)
            oddCase = bloom(s, i, i)
            for case in [longest, evenCase, oddCase]:
                if len(longest) < len(case):
                    longest = case
        return longest
            