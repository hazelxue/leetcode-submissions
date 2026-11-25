class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution(object):
    def minExtraChar(self, s, dictionary):
        """
        :type s: str
        :type dictionary: List[str]
        :rtype: int
        """
        # 1. build trie from dictionary
        root = TrieNode()
        for word in dictionary:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.is_end = True

        # 2. n = len(s); dp = [0] * (n + 1); dp[n] = 0
        n = len(s)
        dp = [0] * (n + 1)

        # 3. for i from n-1 down to 0:
        #      dp[i] = 1 + dp[i+1]                  # skip s[i]
        #      walk the trie from s[i]:
        #        char missing -> break
        #        node.is_end at j -> dp[i] = min(dp[i], dp[j+1])
        for i in range(n - 1, -1, -1):
            dp[i] = 1 + dp[i + 1]
            node = root
            for j in range(i, n):
                if s[j] not in node.children:
                    break
                node = node.children[s[j]]
                if node.is_end:
                    dp[i] = min(dp[i], dp[j + 1])
        return dp[0]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna