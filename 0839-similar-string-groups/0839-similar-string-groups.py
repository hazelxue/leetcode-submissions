class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        father = list(range(n))
        
        # 1.union-find
        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                father[rb] = ra
        
        # 2.similar
        def similar(a, b):
            differ = 0
            for i, j in zip(a, b):
                if i != j:
                    differ += 1
                    if differ > 2:
                        return False
            return differ == 0 or differ == 2
        count = n
        for i in range(n):
            for j in range(i + 1, n):
                if similar(strs[i], strs[j]) and find(i) != find(j):
                    union(i, j)
                    count -= 1
        return count
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna