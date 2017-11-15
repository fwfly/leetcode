class MinStack(object):
    def __init__(self):
        self.stackList = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """

        self.stackList.append(x)
        if not self.minStack :
            self.minStack.append(x)
        elif self.minStack[-1] > x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])


    def pop(self):
        """
        :rtype: void
        """
        self.stackList.pop()
        self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stackList[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
