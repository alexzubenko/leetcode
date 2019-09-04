"""

check if the given string a valid palindrome
simple palindromes examples: "aba", "abba"
"""
class Solution:
    def if_palindrome(self, str):
        for i in range(len(str)//2):
            if str[i] != str[-i-1]:
                return False
        return True

    def if_palindrome_ignore_caps(self, str):
        for i in range(len(str)//2):
            if str[i].lower() != str[-i-1].lower():
                return False
        return True

    def if_palindrome_ignore_punctuation_list(self, str):
        punctuation = ['!', '.', ';', ',']
        without_punctuation = [
            letter for letter in str if letter not in punctuation
        ]
        print(without_punctuation)
        for i in range(len(without_punctuation)//2):
            if without_punctuation[i]!=without_punctuation[-i-1]:
                return False
        return True
    def if_palindrome_ignore_punctuation_string(self, str):
        punctuation = ['!', ';', '.', ',']
        # if we dont want to touch the input string
        # we can copy it to the temp string and replace the punctuation there
        # wiithout_punct = str
        # otherwise change the it in place before palindrome check
        for i in str:
            if i in punctuation:
                str = str.replace(i,'')
        for i in range(len(str)//2):
            if str[i]!=str[-i-1]:
                return False
        return True


sol = Solution()
print(sol.if_palindrome("racecar"))

print(sol.if_palindrome_ignore_caps("RaCeCar"))
print(sol.if_palindrome_ignore_punctuation_list('race;cor!'))
print(sol.if_palindrome_ignore_punctuation_string('race;car'))
