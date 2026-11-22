class union_find(object):
    def __init__(self, n):
        self.father = list(range(n + 1))# index starts at 1
        self.count = n
    def find(self, u):
        if self.father[u] != u:
            self.father[u] = self.find(self.father[u])
        return self.father[u]
    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        self.count -= 1
        self.father[rb] = ra
        return True

class Solution(object):
    def maxNumEdgesToRemove(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        Alice, Bob = union_find(n), union_find(n)
        delete = 0
        for t, u, v in edges:
            if t == 3:
                a = Alice.union(u, v)
                b = Bob.union(u, v)
                if not a and not b:
                    delete += 1
        for t, u, v in edges:
            if t == 1:
                if not Alice.union(u, v):
                    delete += 1
            elif t == 2:
                if not Bob.union(u, v):
                    delete += 1
        
        if Alice.count == 1 and Bob.count == 1:
            return delete
        return -1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna