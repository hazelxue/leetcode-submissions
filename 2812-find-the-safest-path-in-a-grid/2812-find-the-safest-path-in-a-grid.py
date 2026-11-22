class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        # 1. multi-source BFS: distance to the nearest thief
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        
        while q:
            i, j = q.popleft()
            for nx, ny in dir_:
                x, y = i + nx, j + ny
                if 0 <= x < n and 0 <= y < n and dist[x][y] == -1:
                    q.append((x, y))
                    dist[x][y] = dist[i][j] + 1
        
        # 2. union-find
        father = list(range(n * n))
        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                father[rb] = ra
        
        # union dist untill start + end is union
        start, end = 0, n * n - 1
        cells = sorted(((dist[i][j], i, j) for i in range(n) for j in range(n)), reverse=True)
        visited = [[False] * n for _ in range(n)]
        for d, i, j in cells:
            visited[i][j] = True
            idx = i * n + j
            for nx, ny in dir_:
                x, y = i + nx, j + ny
                if 0 <= x < n and 0 <= y < n and visited[x][y]:
                    union(idx, x * n + y)
            if find(start) == find(end):
                return d

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna