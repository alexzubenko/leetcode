"""

We need to reverse the words in sentense aka:

"Hello my dear friend" should transform to "friend dear my Hello"

"""


class Solution:
    def reverse_sent(self, sent):
        print(sent)
        split_sent = sent.split()
        result = ''
        for i in split_sent[::-1]:
            result = result + str(i) + ' '
        return result

    def reverse_sent2(self, sent):
        print(sent)
        return ' '.join(sent.split()[::-1])


sol = Solution()
print(sol.reverse_sent2("Hello my dear friend"))
