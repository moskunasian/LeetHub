class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
       
        # i think a general way to approach this is kadanes algorithm
        # sum values as we iterate over from 1 -> len(nums) - 1, if it isn't negative
       
        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)     
        