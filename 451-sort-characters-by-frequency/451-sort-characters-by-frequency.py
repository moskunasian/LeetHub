class Solution:
    def frequencySort(self, s: str) -> str:
        
        # iterate to find count of each char in str
        # append count of each descending to answer str
        
        answer = ""
        freqDict = {}
        for char in s:
            if char not in freqDict:
                freqDict[char] = 1
            else:
                freqDict[char] += 1
                
        for item in sorted(freqDict.items(), key=lambda item: item[1], reverse=True):
            answer += (item[0] * item[1])
        return answer
        