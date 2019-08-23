class Solution(object):
    def guess(self, input, pick):

        if pick < input:
            return -1 # number is lower
        elif pick > input:
            return 1 # number is higher
        else:
            return 0 # number is equal target

    def guessNumber(self, n):
        left, right = 1, n
        while left <=right:
            mid = (left + right)//2
            print(left)
            print(right)
            print(mid)
            print('---------------------')
            if self.guess(mid,6) == 0:
                return mid
            else:
                if self.guess(mid,6) == -1:
                    right = mid -1
                else:
                    left = mid + 1
        return -1

solution = Solution()
print(solution.guessNumber(10))
