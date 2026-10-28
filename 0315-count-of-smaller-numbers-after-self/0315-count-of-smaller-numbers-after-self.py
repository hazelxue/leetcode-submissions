class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [0] * len(nums)

        def merge_sort(arr):#arr: [val, inital_index]
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            l = merge_sort(arr[:mid])
            r = merge_sort(arr[mid:])

            merge = []
            i, j = 0, 0
            while i < len(l) and j < len(r):
                if r[j][0] < l[i][0]:
                    merge.append(r[j])
                    j += 1
                else:
                    res[l[i][1]] += j
                    merge.append(l[i])
                    i += 1
            
            while i < len(l):#if left part remain, repeat until reach the end
                res[l[i][1]] += j
                merge.append(l[i])
                i += 1
            # if right part remain, just append them
            merge.extend(r[j:])
            return merge
        
        merge_sort([[val, index] for index, val in enumerate(nums)])
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna