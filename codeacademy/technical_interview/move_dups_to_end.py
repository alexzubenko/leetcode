"""

Write a function move_duplicates() which has one parameter: dupe_list.

The argument to move_duplicates() will always be a sorted list which may have duplicated values.

move_duplicates() should move all duplicate values to the end of the list and maintain sorted order.

The return value is the index of the last unique value.


duplicates = ['a', 'a', 'g', 't', 't', 'x', 'x', 'x']
remove_dups(duplicates)
# 3, index of the last unique value: 'x'
duplicates
# ['a', 'g', 't', 'x' 'a', 'x', 't', 'x']

"""

class Solution:
    # This solution checking each number in the list
    # with the next element and if they are the same,
    # Move first element to the array's tail
    def move_deps(self, dups):
        # This counter we need to calculate
        # Last unique index at the end
        initial_counter = len(dups)-1
        # This counter to keep track of how many
        # elements we have checked and stop after we checked
        # all of them
        counter = initial_counter
        # This to calculate how many times we moved the
        # elements, at the end we will use it to find
        # the last unique index
        moves = 0
        # This one to move through the list one by one
        index = 0
        while counter>0:
            if dups[index] == dups[index+1]:
                dups.insert(len(dups),dups.pop(index))
                counter -=1
                moves +=1
            else:
                counter -=1
                index +=1
        print(dups)
        return initial_counter-moves

    #Write a function to leverage the swap technick illustrated in:
        #  https://www.codecademy.com/courses/technical-interview-practice-python/lessons/tip-python-lists/exercises/tip-python-lists-duplicates-no-space?action=resume_content_item



sol = Solution()
print("Starting testing \n")
print("With input {} function should return {} \n and we have {}, which is ===> {}\n".format(
['a', 'a', 'g', 't', 't', 'x', 'x', 'x'], 3,
    sol.move_deps(['a', 'a', 'g', 't', 't', 'x', 'x', 'x']),3 ==
                  sol.move_deps(['a', 'a', 'g', 't', 't', 'x', 'x', 'x'])))


print("With input {} function should return {} \n and we have {}, which is ===> {}\n".format(
['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f'], 4,
    sol.move_deps(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f']),4 ==
                  sol.move_deps(['a', 'a', 'c', 'c', 'd', 'd', 'e', 'e', 'f'])))


print("With input {} function should return {} \n and we have {}, which is ===> {}\n".format(
[13, 13, 13, 13, 13, 42], 1,
    sol.move_deps([13, 13, 13, 13, 13, 42]),1 ==
                  sol.move_deps([13, 13, 13, 13, 13, 42])))