class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        answer = []
        keypad = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        
        def helper(prefix, idx):
            
            # reached end of this current backtrack and isn't just ''
            if idx == len(digits):
                if prefix != '':
                    answer.append(prefix)
                return
            
            for char in keypad[int(digits[idx])]:
                helper(prefix + char, idx + 1)
                
        helper('', 0)
        return answer
        