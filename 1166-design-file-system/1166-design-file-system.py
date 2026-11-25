class TrieNode(object):
    def __init__(self, val=None):#表示接受val传入
        self.children = {}
        self.val = val

class FileSystem(object):

    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path, value):
        """
        :type path: str
        :type value: int
        :rtype: bool
        """
        pas = path[1:].split('/')
        node = self.root
        # 1.(去掉尾)非法路径
        for p in pas[:-1]:
            if p not in node.children:
                return False
            node = node.children[p]
        
        # 2.路径存在了
        if pas[-1] in node.children:
            return False
        
        # 3.True, 建立路径
        node.children[pas[-1]] = TrieNode(val=value)
        return True
                

    def get(self, path):
        """
        :type path: str
        :rtype: int
        """
        pas = path[1:].split('/')
        node = self.root
        for p in pas:
            if p not in node.children:
                return -1
            node = node.children[p]
        return node.val


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna