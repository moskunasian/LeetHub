class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # regular binary search 
        # but now we need to assure that 
        # the number is truly between the left or right range
        
        # have to do this because rotated means 
        # larger wont always be on right and inverse for left side 
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid 
        
            # middle less than what we need
            if nums[mid] < nums[r]:
                # check that target actually on right side
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            # midd larger than what we need
            else:
                # check that target actually on left side
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    