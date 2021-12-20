class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # iterate idx of nums
        # curr target will idx, then two ptrs finding any eligible candidates
        
        ans = set()
        nums.sort()
        
        for i in range(len(nums)):
            
            currTarget = 0 - nums[i]
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                
                # have viable triplet to add
                if nums[l] + nums[r] == currTarget:
                    ans.add((nums[l], nums[r], nums[i]))
                    l += 1
                    r -= 1
                
                # need a larger number to try and reach target
                elif nums[l] + nums[r] < currTarget:
                    l += 1
                    
                # need a smaller number to try and reach target
                else:
                    r -= 1
                    
        return list(ans)    
        
                