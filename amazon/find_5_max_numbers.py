"""
https://www.youtube.com/watch?v=bptRLm3OiV8
Check how does heap works: https://www.codecademy.com/paths/computer-science/tracks/complex-data-structures/modules/cspath-heaps/lessons/conceptual-heaps/exercises/conceptual-heaps-intro
you have many numbers and you need to return max 5

i would say i can see 2 solutions here:
1. sort the list and return last 5 numbers
2. use max() function and add the max element to the
   result list each time and at the same time remove it from the list
"""

def find_max_5_sort(array):
    array.sort()
    return array[:-6:-1]
def find_max_5_remove(array):
    result = []
    for i in range(5):
        result.append(max(array))
        index_to_remove = array.index(max(array))
        array.pop(index_to_remove)
    return result
# write the function to use the min heap which store 5 numbers
# and after that compare each next timber with the root


print(find_max_5_sort([45,66,33,22,111,66,77,88,55,44]))
print(find_max_5_remove([45,66,33,22,111,66,77,88,55,44]))