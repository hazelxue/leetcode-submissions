class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        grid = [[0] * n for _ in range(m)]
        father = list(range(m * n))
        res = []
        count = 0

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            father[rb] = ra

        for i, j in positions:
            if grid[i][j] == 1:
                res.append(res[-1])
                continue
            grid[i][j] = 1
            count += 1
            for nx, ny in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + nx, j + ny
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    ra, rb = find(i * n + j), find(x * n + y)
                    if ra != rb:
                        count -= 1
                        union(ra, rb)
            res.append(count)
        return res



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna