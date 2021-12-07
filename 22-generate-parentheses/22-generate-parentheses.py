class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        # obvious backtracking problem
        # keep track of all combinations given how many open parens 'n' we can have
        
        answer = []
        def backtrack(combo, opened, closed):
            if not opened and not closed:
                answer.append(combo)
            if opened > 0:
                backtrack(combo + '(', opened-1, closed+1)
            if closed > 0:
                backtrack(combo + ')', opened, closed-1)
        backtrack('', n, 0)
        return answer
    