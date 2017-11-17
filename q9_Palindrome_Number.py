class Solution(object):
    def isPalindrome(self, x):

        if x < 0:
            return False
        if x < 10:
            return True

        revert = 0
        while (x > revert):
            revert = revert * 10 + x%10
            if revert == 0:
                return False
            if x > revert:
                x = x/10

        if x == revert:
            return True
        return False
