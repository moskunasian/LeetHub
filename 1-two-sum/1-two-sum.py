class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # iter over vals, saving map of format {target: index}
        targetMap = {}
        for idx, num in enumerate(nums):
            if num not in targetMap:
                targetMap[target - num] = idx
            else:
                return [targetMap[num], idx]
        