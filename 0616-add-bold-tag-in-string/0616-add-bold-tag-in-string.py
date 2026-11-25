class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution(object):
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        # 1. build trie from words
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        # 2. for each start i:
        #      walk the trie along s[i], s[i+1], ...
        #      whenever node.is_end, record farthest end j
        #      mark bold[i..j] = True

        bold = [False] * len(s)
        end = -1#farthest idex where a full word end
        for i in range(len(s)):
            node = root
            for j in range(i, len(s)):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_end:
                    end = j#fond a full word
            for k in range(i, end + 1):#mark bold only if end found
                bold[k] = True
                    
        # 3. build result: add <b> when bold turns on, </b> when it turns off
        res = []
        for i in range(len(bold)):
            if bold[i] and (i == 0 or not bold[i - 1]):
                res.append("<b>")
            res.append(s[i])
            if bold[i] and (i == len(s) - 1 or not bold[i + 1]):
                res.append("</b>")
        return "".join(res)
                

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna