# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def __init__(self):
        self.minnum = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        return self.checkValid(root)

    def checkValid(self, node):

        # Keep go left until find the leftest num
        if node.left is not None:
            res = self.checkValid(node.left)
            if not res:
                return False

        # check and record num
        if self.minnum is None:
            self.minnum = node.val
        else:
            if self.minnum >= node.val:
                return False
            else:
                self.minnum = node.val

        if node.right is not None:
            res = self.checkValid(node.right)
            if not res:
                return False


        return True

node5 = TreeNode(5)
node14 = TreeNode(14)
node1 = TreeNode(1)

node5.left = node14
node14.left = node1
sol = Solution()
print sol.isValidBST(node5)
