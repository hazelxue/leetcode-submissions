class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])
        if m * n == 1:
            return 0
        father = list(range(m * n))# init: father[i] = i

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            father[rb] = ra
        
        # build edges: [weight, idx1, idx2]
        edges = []
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                # right neighbor
                if j + 1 < n:
                    w = abs(heights[i][j] - heights[i][j + 1])
                    edges.append([w, idx, idx + 1])
                # down neighbor
                if i + 1 < m:
                    w = abs(heights[i][j] - heights[i + 1][j])
                    edges.append([w, idx, idx + n])
        
        edges.sort()
        start, end = 0, m * n - 1
        for w, a, b in edges:
            union(a, b)
            if find(start) == find(end):
                return w
        return 0

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna