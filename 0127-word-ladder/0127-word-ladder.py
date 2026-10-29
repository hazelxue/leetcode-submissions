class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}
        while q:
            cur, step = q.popleft()
            if cur == endWord:
                return step
            for i in range(len(cur)):
                for j in "abcdefghijklmnopqrstuvwxyz":
                    tmp = cur[:i] + j + cur[i + 1:]
                    if tmp in wordset and tmp not in visited:
                        q.append((tmp, step + 1))
                        visited.add(tmp)
        return 0


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna