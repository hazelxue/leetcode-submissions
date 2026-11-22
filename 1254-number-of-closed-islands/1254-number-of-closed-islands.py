class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        father = list(range(m * n + 1))
        dummy = m * n
        dir_ = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        def union(a,b):
            ra, rb = find(a), find(b)
            if ra != rb:
                father[rb] = ra
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    continue
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    union(dummy, i * n + j)
                for nx, ny in dir_:
                    x, y = i + nx, j + ny
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                        union(i * n + j, x * n + y)

        count = 0
        root = find(dummy)
        for i in range(m):
            for j in range(n):
                idx = i * n + j
                if grid[i][j] == 0 and father[idx] == idx and idx != root:
                    count += 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna