"""

list = ['a', 'b', 'c', 'd', 'e', 'f']
rotate(list, 1)
# ['b', 'c', 'd', 'e', 'f', 'a']
rotate(list, 4)
# ['e', 'f', 'a', 'b', 'c', 'd']


"""

class Solution:
    def rotate_inplace(self, lst, num_rotations):
        while num_rotations > 0:
            lst.insert(len(lst), lst.pop(0))
            num_rotations -=1
        return lst

    def rotate_inplace_recursion(self, lst, num_rotation):
        if num_rotation < 1:
            return lst
        lst.insert(len(lst), lst.pop(0))
        return self.rotate_inplace_recursion(lst, num_rotation-1)




# Testing
sol = Solution()
print('The following list {} should be transformed to \n'
      ' {} if number of rotation is {},'
      ' in fact we have {} -> {}\n'.format(['a', 'b', 'c', 'd', 'e', 'f'],
       ['a', 'b', 'c', 'd', 'e', 'f'],
       0, sol.rotate_inplace(['a', 'b', 'c', 'd', 'e', 'f'], 0),
       ['a', 'b', 'c', 'd', 'e', 'f'] ==
       sol.rotate_inplace(['a', 'b', 'c', 'd', 'e', 'f'], 0) ))


print('The following list {} should be transformed to \n'
      ' {} if number of rotation is {},'
      ' in fact we have {} -> {} \n'.format(['a', 'b', 'c', 'd', 'e', 'f'],
                                         ['b', 'c', 'd', 'e', 'f', 'a'],
       1, sol.rotate_inplace(['a', 'b', 'c', 'd', 'e', 'f'], 1),
                                         ['b', 'c', 'd', 'e', 'f', 'a'] ==
       sol.rotate_inplace(['a', 'b', 'c', 'd', 'e', 'f'], 1) ))


print('The following list {} should be transformed to \n'
      ' {} if number of rotation is {},'
      ' in fact we have {} -> {}\n'.format(['a', 'b', 'c', 'd', 'e', 'f'],
                                         ['e', 'f', 'a', 'b', 'c', 'd'],
       4, sol.rotate_inplace(['a', 'b', 'c', 'd', 'e', 'f'], 4),
                                         ['e', 'f', 'a', 'b', 'c', 'd'] ==
       sol.rotate_inplace(['a', 'b', 'c', 'd', 'e', 'f'], 4) ))


print('Testing the same but using recursion function:')

print('The following list {} should be transformed to \n'
      ' {} if number of rotation is {},'
      ' in fact we have {} -> {}\n'.format(['a', 'b', 'c', 'd', 'e', 'f'],
       ['a', 'b', 'c', 'd', 'e', 'f'],
       0, sol.rotate_inplace_recursion(['a', 'b', 'c', 'd', 'e', 'f'], 0),
       ['a', 'b', 'c', 'd', 'e', 'f'] ==
       sol.rotate_inplace_recursion(['a', 'b', 'c', 'd', 'e', 'f'], 0) ))


print('The following list {} should be transformed to \n'
      ' {} if number of rotation is {},'
      ' in fact we have {} -> {} \n'.format(['a', 'b', 'c', 'd', 'e', 'f'],
                                         ['b', 'c', 'd', 'e', 'f', 'a'],
       1, sol.rotate_inplace_recursion(['a', 'b', 'c', 'd', 'e', 'f'], 1),
                                         ['b', 'c', 'd', 'e', 'f', 'a'] ==
       sol.rotate_inplace_recursion(['a', 'b', 'c', 'd', 'e', 'f'], 1) ))


print('The following list {} should be transformed to \n'
      ' {} if number of rotation is {},'
      ' in fact we have {} -> {}\n'.format(['a', 'b', 'c', 'd', 'e', 'f'],
                                         ['e', 'f', 'a', 'b', 'c', 'd'],
       4, sol.rotate_inplace_recursion(['a', 'b', 'c', 'd', 'e', 'f'], 4),
                                         ['e', 'f', 'a', 'b', 'c', 'd'] ==
       sol.rotate_inplace_recursion(['a', 'b', 'c', 'd', 'e', 'f'], 4) ))