class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        father = list(range(n))

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        
        count = n
        for a, b in edges:
            ra, rb = find(a), find(b)
            if ra != rb:
                count -= 1
                father[rb] = father[ra]
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna