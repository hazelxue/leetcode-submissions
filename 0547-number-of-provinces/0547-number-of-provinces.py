class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        father = list(range(n))

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                father[rb] = ra
        
        count = n
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1 and find(i) != find(j):
                    union(i, j)
                    count -= 1
        return count


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna