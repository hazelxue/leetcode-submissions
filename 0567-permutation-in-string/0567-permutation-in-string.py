class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        
        need = [0] * 26
        for s in s1:
            idx = ord(s) - ord('a')
            need[idx] += 1
        
        window = [0] * 26
        for i in range(len(s1)):
            idx = ord(s2[i]) - ord('a')
            window[idx] += 1
        
        start = 0
        while start + len(s1) < len(s2):
            if window == need:
                return True
            idx1 = ord(s2[start]) - ord('a')
            window[idx1] -= 1
            idx2 = ord(s2[start + len(s1)]) - ord('a')
            window[idx2] += 1
            start += 1
        return window == need

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna