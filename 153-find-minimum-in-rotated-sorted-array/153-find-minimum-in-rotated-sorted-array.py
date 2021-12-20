class Solution:
    def findMin(self, nums: List[int]) -> int:
       
        l, r = 0, len(nums)-1
        
        if nums[r] > nums[0]:
            return nums[0]
        
        if len(nums) == 1:
            return nums[0]
        
        while l < r:
            mid = (l + r) // 2
            
            # if num to right of mid is smaller, that is inflection pt
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            
            # num before is larger, so midpoint is inflection
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            # if mid is larger than first element, min is somewhere to right
            if nums[mid] > nums[0]:
                l = mid + 1
            else:
                r = mid - 1
            