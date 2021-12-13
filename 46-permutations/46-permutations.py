class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        def dfs(prev, decisions):
            
            print(prev)
            
            # curr permutation is length of orig list
            if len(prev) == len(nums):
                answer.append(list(prev))
                return
            
            # for each val in decisions, dfs down each state 
            # NOT including that given number
            for i in range(len(decisions)):
                prev += [decisions[i]]
                dfs(prev, (decisions[:i] + decisions[i+1:]))
                prev.pop()
        
        dfs([], nums)
        return answer