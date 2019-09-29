"""
find 5 max numbers in the array

use heap

print(find_max_5_remove([45,66,33,22,111,66,77,88,55,44]))

"""

import heapq

# listik = [1,2,3,4,5,4,3,2,5,6,7,7,8]
#
# heap = []
# for i in listik:
#     heapq.heappush(heap,i)
#
# # heapq.heapify(listik)
# #
# # largest_5 = heapq.nlargest(5,listik)
#
# print(heap[::-1])
def fing_five_max(array):
    heapq.heapify(array)
    print(array[:-6:-1])


print(fing_five_max([45,66,33,22,111,66,77,88,55,44]))