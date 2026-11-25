class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # bucket[c]: lists of (word, i): waiting for c
        # index of c in word is i
        bucket = defaultdict(list)
        for word in words:
            bucket[word[0]].append((word, 0))
        res = 0
        for ch in s:
            waiting = bucket.pop(ch, [])#找不到返回[]
            for word, i in waiting:
                i += 1
                if i == len(word):
                    res += 1
                else:
                    bucket[word[i]].append((word, i))
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna