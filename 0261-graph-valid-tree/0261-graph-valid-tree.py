class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        #1.how many edges -> is it link
        if len(edges) != n - 1:
            return False
        
        #2.is it visited?
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = {0}
        q = deque([0])
        while q:
            tmp = q.popleft()
            for num in graph[tmp]:
                if num not in visited:
                    q.append(num)
                    visited.add(num)
        return len(visited) == n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna