class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class StreamChecker(object):
    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()
        max_len = 0
        for word in words:
            node = self.root
            for ch in word[::-1]:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True
            max_len = max(max_len, len(word))
        self.stream = deque(maxlen=max_len)#超过长度，左边弹出

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.append(letter)
        node = self.root
        for ch in reversed(self.stream):
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna