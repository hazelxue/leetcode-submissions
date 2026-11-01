class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        path = []
        result = []

        def dfs(i):#从index开始切是不是回文
            if i == len(s):
                result.append(path[:])
                return
            for j in range(i + 1, len(s) + 1):
                w = s[i : j]
                if w == w[::-1]:
                    path.append(w)
                    dfs(j)
                    path.pop()
        dfs(0)
        return result


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna