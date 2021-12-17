class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        uniqueNums = set(nums)
        maxSeq = 0
        
        for num in nums:
            
            # make sure we are not checking a previous sequence
            if num-1 not in uniqueNums:
                current = num
                distance = 0
                
                while current in uniqueNums:
                    current += 1
                    distance += 1
                    
                maxSeq = max(maxSeq, distance)
        return maxSeq