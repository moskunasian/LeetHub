class MedianFinder:

    def __init__(self):
        self.stream = []
        self.size = 0

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.size += 1

    def findMedian(self) -> float:
        self.stream.sort()
        
        # first retrieve midpoint of stream
        mid = (self.size-1) // 2
        
        # if odd sized datastream can just return mid
        if self.size % 2 != 0:
            return self.stream[mid]
        return (self.stream[mid] + self.stream[mid+1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()