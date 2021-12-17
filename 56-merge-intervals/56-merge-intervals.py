class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # sort the intervals from earliest to latest start times
        # and hold a new list of new potentially 'merged' intervals 
        
        intervals.sort()
        merged = []
        for interval in intervals:
            # if we haven't merged anything or there isn't any overlap
            # just append the current interval!
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # overlap exists, set end time as latest between what's merged and curr interval
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged
        