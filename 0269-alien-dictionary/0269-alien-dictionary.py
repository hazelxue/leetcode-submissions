class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        n = len(words)
        graph = defaultdict(list)
        ingraph = {c:0 for w in words for c in w}
        
        for i in range(n - 1):
            w1, w2 = words[i], words[i + 1]
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    ingraph[w2[j]] += 1
                    break
        
        q = deque([c for c, val in ingraph.items() if val == 0])
        res = []
        while q:
            tmp = q.popleft()
            res.append(tmp)
            for c in graph[tmp]:
                ingraph[c] -= 1
                if ingraph[c] == 0:
                    q.append(c)
        return "".join(res) if len(res) == len(ingraph) else ""

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna