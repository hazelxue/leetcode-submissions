class Solution(object):
    def sequenceReconstruction(self, nums, sequences):
        """
        :type nums: List[int]
        :type sequences: List[List[int]]
        :rtype: bool
        """
        n = len(nums)
        graph = defaultdict(list)
        ingraph = [0] * (n + 1)#index:1...n

        for seq in sequences:
            for u, v in zip(seq, seq[1:]):
                graph[u].append(v)
                ingraph[v] += 1
        
        q = deque([i for i in range(1, n + 1) if ingraph[i] == 0])
        res = []
        while len(q) == 1:
            tmp = q.popleft()
            res.append(tmp)
            for num in graph[tmp]:
                ingraph[num] -= 1
                if ingraph[num] == 0:
                    q.append(num)
        
        return res == nums

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna