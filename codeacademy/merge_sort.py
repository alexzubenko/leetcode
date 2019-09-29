"""

Please implement the merge sort algorithm
thi called divide-and-conquer solution
it consists from two steps:
1. divide the elements of array to small peaces
2. merge those peaces together in the result array

"""

class Solution:

    # Here we will call the merge() function which
    # should do the real work of comparison and
    # merging two arrays to the final one
    def merge(self, left, right):
        print('Merge starts, the inputs here left: {}, right: {} '. format(left,right))
        result = []
        while left and right:
            if left[0] < right[0]:
                result.append(left[0])
                left.pop(0)
            else:
                result.append(right[0])
                right.pop(0)
        if left:
            result += left
        else:
            result += right
        return result

    def merge_sort(self, items):
        # This is going to be our base case for
        # recursive function, merge_sort() will use the recursive calls
        print('Merge_sort starts, the input is: ', items)
        if len(items)< 2:
            return items

        # At first we need to divide the input on two parts
        mid = len(items)//2
        left_part = items[:mid]
        print('left_part is: ', left_part)
        right_part = items[mid:]
        print('right_part is: ', right_part)

        # now we are going to use recursive call to divide
        # the left and right parts even further
        # it will happen as long as the base case is true
        left_shard = self.merge_sort(left_part)
        right_shard = self.merge_sort(right_part)

        # At this point we are invoking the merge()
        # function to get the exact merged list
        return self.merge(left_shard, right_shard)


sol = Solution()
print(sol.merge_sort([1,4,3,2,5,6,7,8]))



