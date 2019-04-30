"""
Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

"""

class Solution(object):
    # here is the solution with zip function
    def longestCommonPrefix(self, strs):
        print(strs)
        print(list(zip(strs)))
        print(list(zip(*strs)))
        pref = ''
        for i in zip(*strs):
            print(i)
            print('----')
            # count = 0
            # for j in i:
            #     if not j == i[0]:
            #         break
            #     count += 1
            # if count == len(i):
            #     pref += i[0]
            if not all(c==i[0] for c in i):
                break
            pref += i[0]
        return pref


    # # this one seems works but leetcode is always complaining about something
    # # moreover this is O(n2) neet to find something better
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     if len(strs) < 2:
    #         return ""
    #     print(len(strs))
    #     check = {}
    #     for i in strs[0]:
    #         check[i] = 0
    #     print(check)
    #     for i in strs:
    #         if i is '':
    #             return ""
    #         for j in i:
    #             if j in check:
    #                 check[j] += 1
    #
    #     print(check)
    #     result = []
    #     # print(len(strs))
    #     for key in check.keys():
    #         if check[key] == len(strs):
    #             result.append(key)
    #     if list(check.values())[0] != len(strs):
    #         return ""
    #     if result:
    #         return "".join(result)
    #     return ""




solution = Solution()
print(solution.longestCommonPrefix(["flower","flow","flight"]))
# print(solution.longestCommonPrefix(["dog","doreti","dom"]))
# print(solution.longestCommonPrefix([""]))
# print(solution.longestCommonPrefix(["",""]))
