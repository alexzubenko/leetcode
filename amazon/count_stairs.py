"""
if you have been given the number of stairs from bottom to the top
and you can take one or two steps at a time
Calculate in how many ways you can clime to the top

"""

# if we look closely to this problem we should see that it is
# perfect example of fibonachi numbers
# in other words the next number = previous + pre_previous
# n = n-1 + n-2

def count_stairs(stairs):
    # we are going to use the recursion
    # here we need to define the base case
    if stairs == 0 or stairs == 1:
        return 1
    else:
        return count_stairs(stairs-1)+ count_stairs(stairs-2)

"""
now we need have been given the number of stairs we should
clime and list of steps we can take to climb
for example stairs = 10, steps = [1,3,5]
the above meanst that we can step 1, 3 or 5 steps at a time, but not 2 
"""

def count_stairs_adv(stairs):
    # at first this problem seems very similat to the previous, so
    # if we have the steps like [1,3,5] we can do something like
    # if stairs ==0:
    #     return 1
    # else:
    #     return count_stairs_adv(stairs-1) + count_stairs_adv(stairs - 3)\
    #            + count_stairs_adv( -5)
    # but the above will not work because if stairs = 1, stairs -3 would be -1
    # so we need to check those numbers before calculation
    steps = [1,2,3]
    if stairs == 0:
        return 1
    total = 0
    for i in steps:
        if stairs -i>=0:
            total += count_stairs_adv(stairs-i)
    return total

print(count_stairs(22))

print(count_stairs_adv(22))