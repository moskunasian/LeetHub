class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charFreq = defaultdict(int)
        i, j = 0, 0
        ans = 0
        
        while j < len(s):
            
            # increment count of current char
            charFreq[s[j]] += 1
            
            # if (total of all seen chars - max of all seen chars) > k
            # means we have utilized all possible 'k' replacements and have to move left-side ptr
            # until there are more 'replacements' available
            while sum(charFreq.values()) - max(charFreq.values()) > k:
                charFreq[s[i]] -= 1
                i += 1
            
            # update the max length at every iteration
            ans = max(ans, j - i + 1)
            j += 1
            
        return ans
            