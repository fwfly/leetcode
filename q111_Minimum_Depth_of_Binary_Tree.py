class Solution(object):

    def __init__(self):
        self.min = 0
        self.cur = 0

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        self.__findMin(root)
        return self.min

    def __findMin(self, node):

        self.cur +=1

        if node.left is not None:
            self.__findMin(node.left)

        if node.right is not None:
            self.__findMin(node.right)

        if node.right is None and node.left is None:
            if self.min == 0:
                self.min = self.cur
            elif self.cur < self.min:
                self.min = self.cur

        self.cur -=1
