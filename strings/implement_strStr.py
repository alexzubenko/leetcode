"""
Implement strStr().

Return the index of the first occurrence of
needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty
string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0
when needle is an empty string. This is consistent to
C's strstr() and Java's indexOf().

"""

class Solution(object):
    # this solution works not for all cases
    # need to check others solutions
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        elif len(needle) > len(haystack):
            return -1
        elif len(needle) == 1 and needle in haystack:
            return haystack.index(needle)

        for i in range(len(haystack)):
            if haystack[i] == needle[0]:
                # print('strating check')
                c = i
                got = False
                j = 1
                # print(haystack[c + 1])
                # print(needle[j])
                while j < len(needle) and c < len(haystack)-1:
                    if haystack[c+1] != needle[j]:

                        got = False
                        break
                    else:
                        got = True
                        j +=1
                        c +=1
                # print('check is over got = ', got)
                if got == True:
                    return i
        return -1




solution = Solution()
print(solution.strStr("hello", "ll"))
print(solution.strStr("mississippi", "issi"))
print(solution.strStr("mississippi", "issipi"))
print(solution.strStr("mississippi", "sippia"))



