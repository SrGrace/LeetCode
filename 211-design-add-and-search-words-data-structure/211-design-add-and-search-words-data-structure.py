class WordDictionary:

    def __init__(self):
        self.tries = {}

    def addWord(self, word: str) -> None:
        node = self.tries
        for w in word:
            node = node.setdefault(w, {})
        node['#'] = True

    def search(self, word: str) -> bool:
        return self.searchNode(self.tries, word)
        
    def searchNode(self, node, word):
        for i, w in enumerate(word):
            if w == '.':
                return any(self.searchNode(node[n], word[i+1:]) for n in node if n != '#')
            if w not in node:
                return False
            node = node[w]
        return '#' in node
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)