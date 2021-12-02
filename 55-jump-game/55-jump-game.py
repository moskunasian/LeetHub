class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # if we start at the end we only need to look for 1 jump
        # if the num available is more than needed, still just need 1
        # if its less, we will need to account for another jump, and can't reach

        
        # one jump edge case
        if len(nums) == 1:
            return True
        
        jumpsNeeded = 1
        canReach = True
        for num in reversed(nums[:-1]):
            if num < jumpsNeeded:
                jumpsNeeded += 1
                canReach = False
            else:
                jumpsNeeded = 1
                canReach = True 
        return canReach
    