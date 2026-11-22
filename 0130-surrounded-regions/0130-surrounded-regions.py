class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        father = list(range(m * n + 1))
        dummy = m * n

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            father[rb] = ra
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                idx = i * n + j
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    union(dummy, idx)
                for nx, ny in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    x, y = i + nx, j + ny
                    if 0 <= x < m and 0 <= y < n and board[x][y] == "O":
                        union(idx, x * n + y)

        root = find(dummy)
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    if find(i * n + j) != root:
                        board[i][j] = "X"


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna