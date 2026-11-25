class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.suggestions = []

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        products.sort()

        # build the trie
        root = TrieNode()
        
        for word in products:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(node.suggestions) < 3:
                    node.suggestions.append(word)
        
        # search
        node = root
        res = []
        for ch in searchWord:
            if node and ch in node.children:
                res.append(node.children[ch].suggestions)
                node = node.children[ch]
            else:
                res.append([])
                node = None#短路
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna