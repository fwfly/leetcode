class Solution(object):
    def smallestDistancePair(self, nums, k):
        def guess(mi):
            count = 0
            left = 0
            rght = 0

            # Slide window
            for right,x in enumerate(nums):
                while x - nums[left] > mi:
                    left += 1

                # sum all possible combinations which distence is less than mi
                count += right - left

            return count >= k

        nums.sort()
        lo = 0
        hi = nums[-1] - nums[0]

        # Binary search
        while lo < hi:

            mi = (hi + lo)/2
            if guess(mi):
                hi = mi
            else:
                lo = mi + 1

        return lo


sol = Solution()
print sol.smallestDistancePair([1,3,1], 1)

