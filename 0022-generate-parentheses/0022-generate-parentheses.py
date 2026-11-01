class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        path = []
        res = []
        def dfs(l, r):
            if r > l or l > n:
                return None
            
            if len(path) == n * 2:
                res.append("".join(path))
                return

            path.append('(')
            dfs(l + 1, r)
            path.pop()

            path.append(')')
            dfs(l, r + 1)
            path.pop()

        
        dfs(0, 0)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna