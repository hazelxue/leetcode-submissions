class Solution(object):
    def wordsAbbreviation(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # rule 1,3
        def abbrev(w, k):
            num = len(w) - k - 1
            if num <= 1:
                return w
            w_abbrev = w[:k] + str(num) + w[-1]
            return w_abbrev
        
        # initialize
        prefix = [1] * len(words)
        res = [abbrev(words[i], 1) for i in range(len(words))]

        # rule 2
        while True:
            group = defaultdict(list)# 缩写 -> 用了这个缩写的单词下标
            for i in range(len(res)):
                group[res[i]].append(i)
            
            conflict = False
            for idxs in group.values():
                if len(idxs) > 1:
                    conflict = True
                    for i in idxs:
                        prefix[i] += 1
                        res[i] = abbrev(words[i], prefix[i])
            if not conflict:
                break
        return res

            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna