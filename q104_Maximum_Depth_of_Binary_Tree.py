
class Solution(object):

    def __init__(self):
        self.max = 0
        self.cur = 0

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.__findMax(root)
        return self.max

    def __findMax(self, node):

        self.cur +=1

        if node.left is not None:
            self.__findMax(node.left)

        if node.right is not None:
            self.__findMax(node.right)

        if self.cur > self.max:
            self.max = self.cur
        self.cur -=1




