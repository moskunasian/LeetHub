class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # iterate over the sorted array
        # save current val as first portion of target
        # closing window from currIdx+1 -> len(nums) - 1
        # since sorted, can close that window depending on what values needed
        answers = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            target = 0 - nums[i]
            while left < right:
                # have found viable triplet and can check further
                if nums[left] + nums[right] == target:
                    answers.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                # need a larger number for possible triplet
                elif nums[left] + nums[right] < target:
                    left += 1
                # need a smaller number for possible triplet
                else:
                    right -= 1
        return list(answers)
        