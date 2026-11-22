class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        father = list(range(m * n))
        #size = [1] * (m * n) is wrong, it could be 0 when grid[i][j] = 0
        size = [grid[i][j] for i in range(m) for j in range(n)]

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return 
            father[rb] = ra
            size[ra] += size[rb]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                idx = i * n + j
                for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = i + nx, j + ny
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        union(idx, x * n + y)
        return max(size)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna