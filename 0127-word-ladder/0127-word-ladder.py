
from sys import setprofile
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordset = set(wordList)#去重
        if endWord not in wordset:
            return 0
        
        q = deque([(beginWord, 1)])
        visited = {beginWord}#避免重复，往回走

        while q:
            word, step = q.popleft()
            if word == endWord:
                return step
            
            for i in range(len(word)):
                for x in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + x + word[i + 1:]
                    if new_word in wordset and new_word not in visited:
                        visited.add(new_word)
                        q.append((new_word, step + 1))
        
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna