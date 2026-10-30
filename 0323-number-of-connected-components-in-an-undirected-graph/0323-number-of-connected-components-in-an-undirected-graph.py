class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        def find_connect(num):
            q = deque([num])
            while q:
                cur = q.popleft()
                for n in graph[cur]:
                    if n not in visited:
                        q.append(n)
                        visited.add(n)    
        
        res = 0
        graph = defaultdict(list)
        visited = set()
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        for i in range(n):
            if i not in visited:
                res += 1
                visited.add(i)
                find_connect(i)
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna