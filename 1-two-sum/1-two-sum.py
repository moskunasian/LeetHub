class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # general how I will approach this is 
        # map of the form { target: index }
        targetMap = {}
        for i, num in enumerate(nums):
            if num not in targetMap:
                targetMap[target - num] = i
            else:
                return [targetMap[num], i]
        