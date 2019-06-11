"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(input):
    if input >= 4:
        return True
    else:
        return False

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 1
        end = n

        while start < end:
            print('start', start)
            print('end',end)

            mid = (start + end)//2
            print('mid',mid)
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
        return start

    # # another slower
    # def firstBadVersion(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     start = 1
    #     while start < n + 1:
    #         if isBadVersion(start):
    #             return start
    #         else:
    #             start += 1
    # this one works fine but for small numbers
    # def firstBadVersion(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     for i in range(1,n+1):
    #         if isBadVersion(i):
    #             print('this version is bad: {}'.format(i))
    #             break
    #         else:
    #             print("thid version is good: {}".format(i))
    #     return i


solution = Solution()
print(solution.firstBadVersion(10))