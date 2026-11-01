class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        n = len(words[0])
        prefix = defaultdict(list)
        for w in words:
            for i in range(n):
                prefix[w[:i]].append(w)
        
        path = []
        res = []
        def dfs(step):
            if len(path) == n:
                res.append(path[:])
                return
            
            pre = "".join(word[step] for word in path)
            for x in prefix[pre]:
                path.append(x)
                dfs(step + 1)
                path.pop()
        dfs(0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna