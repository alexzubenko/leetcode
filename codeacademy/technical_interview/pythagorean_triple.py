"""
the main idea is to check if we have given a,b and c
is the following formula is true:

a^2 + b^2 = c^2


"""

class Solution(object):
    # this is the ideal case when we have exact 3 numbers as an input
    def check_triplet(self, a,b,c):
        if a**2 + b**2 == c**2:
            print(a**2)
            print(b**2)
            print(c**2)
            return True
        return False

    def check_triplet_list(self, triplet):
        # this is the ideal situation when we should expect only 3 numbers
        # in the triplet
        # first we need to check if the triplet is the triplet
        # in other words if it contains 3 numbers and if no we should
        # return False
        if len(triplet)!=3:
            return False
        # get rid of negative numbers we need to worry only for the absolute values
        for i in range(len(triplet)):
            if triplet[i]<0:
                triplet[i] = abs(triplet[i])
        if triplet[0]**2 + triplet[1]**2 == triplet[2]**2:
            return True
        return False

    def check_triplet_list_big_than_three(self, triplet):
        print(triplet)
        # the following will not work in case if the input is not sorted
        # therefor we should sort the list first
        triplet.sort()
        print(triplet)
        for i in range(len(triplet)):
            for j in range(i+1,len(triplet)):
                for k in range(j+1,len(triplet)):
                    print('Triplet we are going to check {}**2 + {}**2 = {}**2  === {} + {} ?= {}'.format(
                        triplet[i], triplet[j], triplet[k], triplet[i]**2, triplet[j]**2, triplet[k]**2, ))
                    if triplet[i]**2 + triplet[j]**2 == triplet[k]**2:
                        print('here is the triplet {}**2 + {}**2 = {}**2'.format(
                            triplet[i],triplet[j],triplet[k]))
                        return True
        return False


sol = Solution()
print(sol.check_triplet(3,4,5))
print(sol.check_triplet_list([-3,-4,-5]))
print(sol.check_triplet_list([-3,-4]))

print(sol.check_triplet_list_big_than_three([5,4,3]))
# print(sol.check_triplet_list_big_than_three([2]))
