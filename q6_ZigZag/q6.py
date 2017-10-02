class Solution(object):
    def convert(self, s, numRows):
        """
            :type s: str
            :type numRows: int
            :rtype: str
         """

        if numRows == 1:
            return s

        # create a list which length is based on numRows
        zaglist = ['']*numRows
        #print zaglist


        # loop all cahrastic and assign it into list
        # where based on raw number
        idx = 0
        op = 1

        for c in s:

            zaglist[idx] = zaglist[idx] + c

            idx = idx + op
            if idx == 0:
                op = 1
            elif idx == numRows -1:
                op = -1

        res = ""
        for z_str in zaglist:
            if z_str != '' and z_str != '"':
                res = res + z_str

        print res
        return res

sol = Solution()
#sol.convert("PAYPALISHIRING", 3)
sol.convert("A",2)

