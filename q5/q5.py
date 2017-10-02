#Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
#Example:
#
#    Input: "babad"
#
#    Output: "bab"
#
#    Note: "aba" is also a valid answer.
#
#    Example:
#
#        Input: "cbbd"
#
#        Output: "bb"
#


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s:str
        :rtype s:str
        """
        res = [0]

        # insert # in string
        # string will be #a#b#c#
        t = iter(s)
        p = '#' +  '#'.join(a  for a in s ) + '#' # O(n)
        #print p

        # search bigest value
        # O(n)
        s_len = len(p)

        pl_value = 0
        pl_idx = -1

        #if s_len == 3:
        #    return s

        for idx, c in enumerate(p):
            if idx:
                pl = 0
                for pi in range(1, idx+1): # from 1 to idx
                    #print "%d %d," % (idx - pi, idx + pi),
                    if idx + pi < s_len:
                        if p[idx - pi] == p[idx + pi]:
                            pl +=1
                        else:
                            break
                    else:
                        break

                if pl > pl_value:
                    pl_value = pl
                    pl_idx = idx

        #print "%d, %d"% (pl_idx, pl_value)
        #print "%d, %d"% (pl_idx - pl_value, pl_idx + pl_value)
        res = p[pl_idx - pl_value : pl_idx + pl_value + 1]
        res =  ''.join(res.split('#'))
        #if len(res) == 1:
        #    return ""
        print res
        return res


sol = Solution()
sol.longestPalindrome("abcda")

