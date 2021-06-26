
# 用 while 重寫

class Solution(object):
    def  findLength(self, nums1, nums2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """

        i1 = 0
        i2 = 0
        v1 = 0
        v2 = 0
        p1 = 0
        p2 = 0
        len1 = len(nums1)
        len2 = len(nums2)
        max_sub = 0

        while(i1 < len1):
            max_sub_tmp = 0
            v1 = nums1[i1]
            i2 = 0
            while(i2 < len2):
                #print(f"find next----{p1}: {len1}, {p2}: {len2}, {i1}, {i2}")
                v2 = nums2[i2]
                if v1 == v2:
                    p1 = i1
                    p2 = i2
                    while(p1 < len(nums1) and p2 < len(nums2)):
                        #print(f"{nums1[p1]}: {p1}, {nums2[p2]}: {p2}")
                        if nums1[p1] != nums2[p2]:
                            if max_sub_tmp > max_sub:
                                max_sub = max_sub_tmp
                            #print(f"max: {max_sub_tmp}")
                            max_sub_tmp = 0
                            break
                        p2 = p2 + 1
                        p1 = p1 + 1
                        max_sub_tmp = max_sub_tmp + 1
                    
                i2 = i2 + 1

                if max_sub_tmp > max_sub:
                    #print(max_sub_tmp)
                    max_sub = max_sub_tmp
                max_sub_tmp = 0
            i1 = i1 + 1
        return max_sub
    


sol = Solution()
print(sol.findLength([1,2,3,2,1], [3,2,1,4,7]))
print(sol.findLength( [0,1,1,1,1], [1,0,1,0,1]))
print(sol.findLength([0,0,0,0,0,0,1,0,0,0, 2], [0,0,0,0,0,0,0,1,0,0, 3]))
