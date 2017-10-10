# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def __init__(self):
        self.res = []

    def traverse(self, node):


        if not node.left:
            pass
        else:
            self.traverse(node.left)

        self.res.append(node.val)

        if not node.right:
            pass
        else:
            self.traverse(node.right)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        if not root:
            return []

        if not root.left:
            pass
        else:
            self.traverse(root.left)

        self.res.append(root.val)

        if not root.right:
            pass
        else:
            self.traverse(root.right)

        return self.res



