"""

Given a string, determine if it is a palindrome,
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define
empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false

"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        punctuation = [' ', ',', '.', ':', '@', '/', "#", '-', '?', "\\", "\"", "\'", ";", "!", "(", ")", "`"]
        no_punct = s.replace(" ", "")
        no_punct = no_punct.lower()
        for i in punctuation:
            if i in no_punct:
                no_punct = no_punct.replace(i,"")
        i = 0
        while i < len(no_punct)/2:
            if no_punct[i] != no_punct[-(i+1)]:
                return False
            i +=1
        return True



solution = Solution()
# print(solution.isPalindrome("A man, a plan, a canal: Panama"))
print(solution.isPalindrome("A man, a plan, a canal: Panama"))