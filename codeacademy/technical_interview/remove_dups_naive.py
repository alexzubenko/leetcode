"""

Given a list of values with duplicates, return a list holding the same values
in the same order with all duplicates removed.

duplicates = ['a', 'a', 'x', 'x', 'x', 'g', 't', 't']
remove_dups(duplicates)
# ['a', 'x', 'g', 't']

more_duplicates = [3, 3, 1, 7, 7, 7]
remove_dups(more_duplicates)
# [3, 1, 7]

"""

class Solution:
    # Naive solution with additional array, which means it is:
    # Time complexity = O(N) - we are checking all elements
    # Space complxity = O(N) - we are creating new list of n elements
    def remove_dups(self, dup_list):
        result = []
        for i in dup_list:
            if i not in result:
                result.append(i)
        return result

    # This solution should amend the initial array in
    # place and do not allocate additional memory like
    # in the solution above
    def remove_inplace(self, dup_list):
        # Due to fact that counter here represents
        # the last valid index of array we should substitute 1
        # from it to not hit the index out of range error
        counter = len(dup_list)-1
        index = 0
        while index < counter:
            if dup_list[index] == dup_list[index + 1]:
                dup_list.pop(index)
                counter -=1
            else: index +=1
        return dup_list

    # Write the function which should leverage .count() built in list method




sol = Solution()
print('Starting testing')
print("{} should transform to {}\n"
      " and we have {}, which is actually ==> {}\n".format(
    ['a', 'a', 'x', 'x', 'x', 'g', 't', 't'],
    ['a', 'x', 'g', 't'], sol.remove_dups(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']),
    ['a', 'x', 'g', 't'] ==  sol.remove_dups(['a', 'a', 'x', 'x', 'x', 'g', 't', 't'])))

print("{} should transform to {}\n"
      " and we have {}, which is actually ==> {}\n".format(
    [3, 3, 1, 7, 7, 7],
    [3, 1, 7], sol.remove_dups([3, 3, 1, 7, 7, 7]),
    [3, 1, 7] ==  sol.remove_dups([3, 3, 1, 7, 7, 7])))

print('\nStarting testing solution in place\n')
print("{} should transform to {}\n"
      " and we have {}, which is actually ==> {}\n".format(
    ['a', 'a', 'x', 'x', 'x', 'g', 't', 't'],
    ['a', 'x', 'g', 't'], sol.remove_inplace(['a', 'a', 'x', 'x', 'x', 'g', 't', 't']),
    ['a', 'x', 'g', 't'] ==  sol.remove_inplace(['a', 'a', 'x', 'x', 'x', 'g', 't', 't'])))


print("{} should transform to {}\n"
      " and we have {}, which is actually ==> {}\n".format(
    [3, 3, 1, 7, 7, 7],
    [3, 1, 7], sol.remove_inplace([3, 3, 1, 7, 7, 7]),
    [3, 1, 7] ==  sol.remove_inplace([3, 3, 1, 7, 7, 7])))