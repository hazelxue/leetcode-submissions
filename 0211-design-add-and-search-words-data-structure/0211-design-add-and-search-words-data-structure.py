class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary(object):
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def dfs(self, node, word, i):#从节点 node 出发，能不能匹配 word[i:]？
        if i == len(word):
            return node.is_end
        
        ch = word[i]
        if ch != '.':
            if ch not in node.children:
                return False
            return self.dfs(node.children[ch], word, i + 1)

        for child in node.children.values():
            if self.dfs(child, word, i + 1):
                return True
        return False

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.dfs(self.root, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna