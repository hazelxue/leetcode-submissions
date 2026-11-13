class FirstUnique(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.dic = {}
        self.i = 0
        for num in self.nums:
            self.dic[num] = self.dic.get(num, 0) + 1


    def showFirstUnique(self):
        """
        :rtype: int
        """
        while self.i < len(self.nums) and self.dic[self.nums[self.i]] > 1:
            self.i += 1
        if self.i < len(self.nums):
            return self.nums[self.i]
        return -1
        

    def add(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.nums.append(value)
        self.dic[value] = self.dic.get(value, 0) + 1     


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna