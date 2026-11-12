class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        m, n = len(heightMap), len(heightMap[0])
        water = 0
        visited = [[False] * n for _ in range(m)]
        heap = []#存放墙，每个点一次push 一次Pop
        #1.外圈
        for i in range(m):
            for j in range(n):
                if i in [0, m - 1] or j in [0, n - 1]:
                    visited[i][j] = True
                    heapq.heappush(heap, (heightMap[i][j], i, j))
        #2.找墙的最低点
        while heap:
            val, i, j = heapq.heappop(heap)
            for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx, ny = i + x, j + y
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (max(heightMap[nx][ny], val), nx, ny))#这里墙要更新，取高的
                    water += max(0, val - heightMap[nx][ny])
        return water

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna