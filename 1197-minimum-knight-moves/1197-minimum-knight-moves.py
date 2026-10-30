class Solution(object):
    def minKnightMoves(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        visited = {(0, 0)}
        q = deque([(0, 0, 0)])#(x, y, step)
        directions = [(2, 1), (1, 2), (-2, -1), (-1, -2), (-2, 1), (-1, 2), (2, -1), (1, -2)]
        x, y = abs(x), abs(y)

        while q:
            nx, ny, step = q.popleft()
            if nx == x and ny == y:
                return step
            for a, b in directions:
                i, j = nx + a, ny + b
                if -2 <= i and -2 <= j and (i, j) not in visited:
                    visited.add((i, j))
                    q.append([i, j, step + 1])
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna