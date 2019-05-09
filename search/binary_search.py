"""
this is the prototype of binary search
"""


class Solution(object):
    def binarySearch(self, listik, n):
        middle = len(listik)//2
        if n < middle:
            listik = listik[:middle]
        elif n > middle:
            listik = listik[middle:]
        else:
            return middle
        print(listik)


solution = Solution()
print(solution.binarySearch([1,2,3,4,5,6,7,8,9,10,11], 5))