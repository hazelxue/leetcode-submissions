class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        m, n = len(s), len(p)
        if m < n:
            return []
        need = [0] * 26
        have = [0] * 26
        res = []
        for ch in p:
            need[ord(ch) - ord('a')] += 1
        
        # sliding window
        for i in range(m):
            have[ord(s[i]) - ord('a')] += 1
            if i >= n:
                have[ord(s[i - n]) - ord('a')] -= 1
            if have == need:
                res.append(i - n + 1)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna