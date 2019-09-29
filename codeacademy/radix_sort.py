class Solution:
    def radix_sort(self, arr):
        max_value = max(arr)
        max_exponent = len(str(max_value))
        return max_exponent




sol = Solution()
print(sol.radix_sort([1,2,3,4,5]))