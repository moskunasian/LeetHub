class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # convert to lowercase, no spaces, no non-alphanumeric
        converted = ""
        for i in s:
            if i != " ":
                if i.isalnum():
                    converted += i.lower()
        
        # two pointers from left/right, if ever unequal not palindrome
        left, right = 0, len(converted) - 1
        while left < right:
            if converted[left] != converted[right]:
                return False
            left += 1
            right -= 1
        return True