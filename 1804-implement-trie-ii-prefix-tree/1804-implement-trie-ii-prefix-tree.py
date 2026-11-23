class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = 0
        self.pass_ = 0

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]#先走再加，因为root不需要计数
            node.pass_ += 1
        node.end += 1

    def find(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        res = self.find(word)
        if res is not None:
            return res.end
        return 0

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res = self.find(prefix)
        if res is not None:
            return res.pass_
        return 0

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            node = node.children[ch]
            node.pass_ -= 1
        node.end -= 1


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna