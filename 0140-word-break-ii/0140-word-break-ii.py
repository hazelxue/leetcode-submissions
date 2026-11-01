class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        wordset = set(wordDict)
        memo = {}

        def dfs(i):
            if len(s) == i:
                return [""]
            if i in memo:
                return memo[i]
            
            res = []
            for j in range(i + 1, len(s) + 1):
                w = s[i : j]
                if w in wordset:
                    for ws in dfs(j):
                        res.append(w + " " + ws if ws else w)
            memo[i] = res
            return res
        return dfs(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna