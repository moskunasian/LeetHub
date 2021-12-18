class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        # same as find duplicate in array
        # not we just have a list we can return every time we encounter a negative
        
        ans = []
        for i in range(len(nums)):
            changeIdx = abs(nums[i]) - 1
            if nums[changeIdx] < 0:
                ans.append(changeIdx+1)
            else:
                nums[changeIdx] *= -1
        return ans
    