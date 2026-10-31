class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordset = set(wordList)
        if endWord not in wordset:
            return []

        #1.bfs
        graph = defaultdict(list)
        layer = {beginWord}
        wordset -= layer
        found = False

        while layer and not found:
            next_layer = set()
            for u in layer:
                for k in range(len(u)):
                    for x in "abcdefghijklmnopqrstuvwxyz":
                        v = u[:k] + x + u[k + 1:]
                        if v in wordset:
                            next_layer.add(v)
                            graph[v].append(u)
                        if v == endWord:#先加入结果再判断，还是都可以？
                            found = True
            wordset -= next_layer
            layer = next_layer
        
        #2.dfs
        res = []
        path = [endWord]
        
        def dfs(word):
            if word == beginWord:
                res.append(path[:][::-1])
                return
            for u in graph[word]:
                path.append(u)
                dfs(u)
                path.pop()
        dfs(endWord)
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna