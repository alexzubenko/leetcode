"""

we need to write the function to implement bubble sort
algorithm in python, in outher words we will swipe the elements
if the first > next
"""

class Solution:
    # this is the helper function to swap values
    def swap(self, arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]

    # this is the main function
    # after one pass we will have the greatest value at
    # end of the array, and array is still not fully sorted,
    # it means we should start from the beginning of the list again
    # and recheck all values and do it as many time before all
    # the elements are in order
    # hence we need to perform as many passes as elements
    # in the input array (that is for thid code: (for i in arr:) )
    def bubble_sort(self, arr):
        print(arr)
        for i in arr:
            for index in range(len(arr)-1):
                print('checking values {}:{}'.format(arr[index], arr[index+1]))
                if arr[index]> arr[index+1]:
                    self.swap(arr,index,index+1)
        return arr
    # write the optimize version when we dont need to recheck the
    # last element in each iteration because after first iteration the
    # last element will be the biggest any way
    # compare the iterations count with the above version of the function

sol = Solution()
print(sol.bubble_sort([1,23,4,5,6]))
