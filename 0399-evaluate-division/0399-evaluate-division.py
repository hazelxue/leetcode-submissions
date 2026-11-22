class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # "abc" so we cound not use list, but dict
        father = {}
        weight = {}#weight[x] = x / father[x]

        def add(x):#initialize
            if x not in father:
                father[x] = x
                weight[x] = 1

        def find(x):# find root with path compression
            if father[x] != x:
                p = father[x]
                root = find(p)
                weight[x] *= weight[p]#update weight to x / root( = x/p * p/root)
                father[x] = root
            return father[x]
        
        def union(a, b, k):# record a / b = k
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            father[ra] = rb
            # weight[ra] = (ra / a) * (a / b) * (b / rb) 
            # = (1 / weight[a]) * k * weight[b]
            weight[ra] = k * weight[b] / weight[a]
        
        for (a, b), k in zip(equations, values):
            add(a)
            add(b)
            union(a, b, k)
        
        res = []
        for x, y in queries:
            if x not in father or y not in father or find(x) != find(y):
                res.append(-1.0)
            else:
                # same root: x/y = (x/root) / (y/root)
                res.append(weight[x] / weight[y])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna