class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordset = set(wordDict)
        memo = {}

        def dfs(i):
            if i == len(s):
                return True
            if i in memo and not memo[i]:
                return False
            
            for j in range(i + 1, len(s) + 1):
                w = s[i:j]
                if w in wordset and dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False      
            return False
        
        return dfs(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna