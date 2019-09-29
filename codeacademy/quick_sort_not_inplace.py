"""
This is the easy way of quick sort implementation
where we dont need to do everything in place
basically we will crate who lists to store the data
and at the enc we will return them list1 + list2


"""

class Solution:
    def quicksort(self, list):
        if len(list)<=1:
            return list

        left_portion = []
        right_portion = []

        pivot = 0
        pivot_element = list[pivot]
        for i in range(1, len(list)):
            if list[i]< list[pivot]:
                left_portion.append(list[i])
            else:
                right_portion.append(list[i])

        sorted_smaller = self.quicksort(left_portion)
        print('sorted_smaller: ', sorted_smaller)
        sorted_bigger = self.quicksort(right_portion)

        return sorted_smaller + [pivot_element] + sorted_bigger


sol = Solution()
print(sol.quicksort([1,3,2,4,3,5,2,6]))

