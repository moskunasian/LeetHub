class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        tmp = self.trie
        for char in word:
            if char not in tmp:
                tmp[char] = {}
            tmp = tmp[char]
        tmp['end'] = True

    def search(self, word: str) -> bool:
        tmp = self.trie
        for char in word:
            if char in tmp:
                tmp = tmp[char]
            else:
                return False
        return 'end' in tmp
            

    def startsWith(self, prefix: str) -> bool:
        tmp = self.trie
        for char in prefix:
            if char in tmp:
                tmp = tmp[char]
            else:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)