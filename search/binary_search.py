"""
this is the prototype of binary search
"""


class Solution(object):
    # this one was written just for fun and does not work like real search
    # it counts only iterations and is not giving the position where target is
    # in order to add this functionality we should add additional array here
    def binarySearch(self, listik, n):
        print('initial list: ', listik)
        iteration = 1
        while len(listik) > 1:
            print('iteration: ', iteration)
            print('we need to find = ', n)
            middle = len(listik)//2
            # print('middle = ', middle)
            if n == listik[middle]:
                print('we found: ',listik[middle])
                return 'hurrayyy we got it'
            if n < listik[middle]:
                listik = listik[:middle]
            elif n > listik[middle]:
                listik = listik[middle:]
            print(listik)
            iteration +=1


solution = Solution()
# print(solution.binarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17], 17))
print(solution.binarySearch([-1, 0, 3, 5, 9, 12, 31, 333, 433, 555, 777], 333))