"""

Given a string, find the first non-repeating
character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

"""


class Solution(object):
    # the following solution works, but not for huge inputs
    # def firstUniqChar(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     for i in s:
    #         if s.count(i)==1:
    #             return s.index(i)
    #     return -1
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniq = {}
        for i in s:
            if i in uniq:
                uniq[i] = 0
            else:
                uniq[i] = 1
        for i in range(len(s)):
            if uniq[s[i]]==1:
                return i
        return -1




solution = Solution()
print(solution.firstUniqChar("loveleetcode"))