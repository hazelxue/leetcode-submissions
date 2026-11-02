class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        graph = defaultdict(list)
        for f, t in sorted(tickets, reverse=True):
            graph[f].append(t)
        
        res = []
        def dfs(airport):
            if not graph[airport]:
                res.append(airport)
                return
            
            while graph[airport]:
                tmp = graph[airport].pop()
                dfs(tmp)
            res.append(airport)
            return
        
        dfs("JFK")
        return res[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna