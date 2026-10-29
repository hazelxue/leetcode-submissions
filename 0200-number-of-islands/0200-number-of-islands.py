class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        island = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    island += 1
                    q = deque([(i, j)])
                    grid[i][j] = "0"
                    while q:
                        r, c = q.popleft()
                        for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                            if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                                q.append((x, y))
                                grid[x][y] = "0"
        return island

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna