class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        cur = 1
        pre = 1
        i = 1
        while( i < n ):
            temp = cur
            cur = cur + pre
            pre = temp`
            i += 1
        return cur

sol =  Solution()
print sol.climbStairs(1)
print sol.climbStairs(2)
