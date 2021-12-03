
# idea is to use a Trie
# whenenever we hit a '.', recursively search all children

class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        tmp = self.trie
        for c in word:
            if c not in tmp:
                tmp[c] = {}
            tmp = tmp[c]
        tmp['end'] = {}

    def search(self, word: str) -> bool:
        def helper(word, position, t):
            
            # if position in search longer than word
            # return a check if we hit end or not 
            if position >= len(word):
                return 'end' in t
            
            # wildchar case check
            if word[position] == '.':
                print(t.keys())
                for k in t.keys():
                    if helper(word, position+1, t[k]):
                        return True
            else:
                if word[position] not in t:
                    return False
                else:
                    return helper(word, position+1, t[word[position]])
        return helper(word, 0, self.trie)
            