class Solution:
    def countSubstrings(self, s: str) -> int:
        
        # same general idea as finding any palindromic substring
        # now we are just counting the amount that exist in total
        # for each letter we bloom out counting and incrementing per each palindrom
        # and return that count for the current letter and keep it w/ overall total
        # main thing we have to think about it even (i & i+1) and odd (just i) cases
        
        def checkPalindrome(l, r, s):
            count = 0
            while (l >= 0) and (r < len(s)) and (s[l] == s[r]):
                count += 1
                l -= 1
                r += 1
            return count
        
        numPalSub = 0
        for i in range(len(s)):
            numPalSub += checkPalindrome(i, i + 1, s)
            numPalSub += checkPalindrome(i, i, s)
        return numPalSub    
        