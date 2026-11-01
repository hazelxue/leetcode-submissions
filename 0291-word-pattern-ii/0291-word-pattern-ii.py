class Solution(object):
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        ch_to_word = {}
        used = set()

        def dfs(i, j):
            if i == len(pattern) and j == len(s):
                return True#最内层的return值，也叫终止条件
            if i == len(pattern) or j == len(s):
                return False
            
            p = pattern[i]
            #case1
            if p in ch_to_word:
                if s.startswith(ch_to_word[p], j):
                    return dfs(i + 1, j + len(ch_to_word[p]))
                return False
            
            #case2
            for k in range(j + 1, len(s) + 1):
                w = s[j: k]
                if w in used:
                    continue
                ch_to_word[p] = w
                used.add(w)
                if dfs(i + 1, k):
                    return True#层层向外汇报true，最终（0,0）这里会收到true的大结果
                del ch_to_word[p]
                used.remove(w)
            return False
        
        return dfs(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna