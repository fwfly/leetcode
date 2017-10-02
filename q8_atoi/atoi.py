class Solution(object):
        def myAtoi(self, str_num):
            """
             :type str: str
             :rtype: int
             :
             : +-
             : 01234
             : 001234
            """
            if not str_num :
                return 0

            op=1
            c = str_num[0]

            # filter empty
            for idx, c in enumerate(str_num):
                if c.isspace():
                    pass
                else:
                    str_num = str_num[idx :]
                    break

            # check operation
            if c == "-":
                op=-1
                str_num = str_num[1:] # remove operator
            elif c == "+":
                str_num = str_num[1:] # remove operator

            # filter 0
            for idx, c in enumerate(str_num):

                if ord(c) >= 48 and ord(c)<= 57:
                    if c != "0":
                        str_num = str_num[idx :]
                        break
                else:
                    return 0

            res=0
            for idx, c in enumerate(str_num):
                if ord(c) >= 48 and ord(c)<= 57:
                    c_num = ord(c) - 48
                    if idx:
                        res = res*10
                    res = res + c_num
                else:
                    break

            res = res*op
            if res > 2147483647:
                return 2147483647
            if res < -2147483648:
                return -2147483648

            return res


sol=Solution()
print sol.myAtoi("   +22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa22aa")
print sol.myAtoi("    19933")
print sol.myAtoi("  -0012a42")
print sol.myAtoi("2147483647")
#sol.myAtoi("1")
#sol.myAtoi("-0110")
