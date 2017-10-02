class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # Symbol  I   V   X   L   C   D    M
        # Value   1   5   10  50  100 500  1,000

        # Number      4   9   40  90  400 900
        # Notation    IV  IX  XL  XC  CD  CM

        # zero nulla
        roman = ""

        if num == 0:
            return "nulla"

        # divide 1000
        res = num/1000
        if res != 0:
            roman = roman + 'M'*res
        num = num - res * 1000

        # divide 100
        res = num/100
        if res != 0:
            if res == 9:
                roman = roman + "CM"
            elif res == 4:
                roman = roman + "CD"
            elif res == 5:
                roman = roman + "D"
            else:
                mul = res
                if res > 5:
                    roman = roman + "D"
                    mul = res -5
                roman = roman + "C"*mul
        num = num - res*100

        # divide 10
        res = num/10
        if res != 0:
            if res == 9:
                roman = roman + "XC"
            elif res == 4:
                roman = roman + "XL"
            elif res == 5:
                roman = roman + "L"
            else:
                mul = res
                if res > 5:
                    roman = roman + "L"
                    mul = res -5
                roman = roman + "X"*mul
        num = num - res*10

        if num != 0:
            if num == 9:
                roman = roman + "IX"
            elif num == 4:
                roman = roman + "IV"
            elif num == 5:
                roman = roman + "V"
            else:
                mul = num
                if num > 5:
                    roman = roman + "V"
                    mul = num -5
                roman = roman + "I"*mul

        return roman


sol = Solution()
print sol.intToRoman(3999)
print sol.intToRoman(1000)



