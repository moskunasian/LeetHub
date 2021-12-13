class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupGram = {}
        for gram in strs:
            sg = "".join(sorted(gram))
            if sg not in groupGram:
                groupGram[sg] = [gram]
            else:
                groupGram[sg].append(gram)
        return [v for k, v in groupGram.items()]
            