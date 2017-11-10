class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sigNum = None
        nums.sort()

        for idx, num in enumerate(nums):
            if (idx%2) == 0:
                sigNum = num
            else:
                if sigNum != num:
                    return sigNum
        return sigNum
