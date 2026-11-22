class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        n = len(accounts)
        father = list(range(n))
        email_to_id = {}# fist-time id

        def find(u):
            if father[u] != u:
                father[u] = find(father[u])
            return father[u]
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra != rb:
                father[rb] = ra
        
        # 1. Seen this email before? Then union with that account
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in email_to_id:
                    union(email_to_id[email], i)
                else:
                    email_to_id[email] = i
        
        # 2. Group emails by root, then format
        groups = defaultdict(list)
        for email, idx in email_to_id.items():
            groups[find(idx)].append(email)
        return [[accounts[idx][0]] + sorted(email) for idx, email in groups.items()]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna