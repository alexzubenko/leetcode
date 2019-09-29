"""
https://www.youtube.com/watch?v=bptRLm3OiV8

given an array of numbers in sorted order
count the pairs of numbers whose sum is less than X
for example: [2,4,6,8,9], the x=14
"""
class Solution:
    # this one is simple but slow with complexity O(n2)
    def count_pairs(self, array, x):
        count = 0
        for i in range(len(array)):
            for j in range(i+1, len(array)):
                if array[i] + array[j] < x:
                    # print('{} + {} < {}'.format(array[i],array[j],x))
                    count +=1
        return count
    # create the function with memory complexity O(n):
    def count_pairs_smart(self, array, x):
        first = 0
        last = len(array)-1
        count = 0
        while first <=last:
            if array[first]+ array[last]< x:
                count += last - first
                first +=1
            else:
                last -=1
        return count

sol = Solution()
print(sol.count_pairs([2,4,6,8,9],14))
print(sol.count_pairs_smart([2,4,6,8,9], 14))