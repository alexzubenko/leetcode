"""
Given two strings s and t ,
write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters?
How would you adapt your solution to such case?

"""
from collections import Counter

class Solution(object):
    # this one works, but consumes huge amount of memory
    # def isAnagram(self, s, t):
    #     """
    #     :type s: str
    #     :type t: str
    #     :rtype: bool
    #     """
    #     t = list(t)
    #     if len(s) != len(t):
    #         return False
    #     for i in range(len(s)):
    #         if s[i] in t:
    #             t.pop(t.index(s[i]))
    #     if len(t)<1:
    #         return True
    #     return False
    # The following solution with Counter
    # def isAnagram(self, s, t):
    #     if len(s) != len(t):
    #         return False
    #     if Counter(s) == Counter(t):
    #         return True
    #     return False
    # the following example we are using two dictionaries and compareing them
    # dict1.get(i,5) + 1 - means it is searching for i to get it and if
    # i is not in the dict the default value will be 5
    # def isAnagram(self, s, t):
    #     dict1 = {}
    #     for i in s:
    #         dict1[i] = dict1.get(i,5) + 1
    #     dict2 = {}
    #     for i in t:
    #         dict2[i] = dict2.get(i,5) + 1
    #     print(dict1)
    #     print(dict2)
    #     if dict1 == dict2:
    #         return True
    #     return False
    # Here we can compare two lists, but at first we should sort them
    def isAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        return False






solution = Solution()
print(solution.isAnagram("aacc", "ccaa"))