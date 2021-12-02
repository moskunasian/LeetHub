class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # general idea is to start baseline of largest container possible
        # constrict window on smaller side until they cross each other
        # keeping track of max along the way
        left, right = 0, len(height) - 1
        maxWater = 0
        while left < right:
            water = (right - left) * (min(height[left], height[right]))
            maxWater = max(maxWater, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
        