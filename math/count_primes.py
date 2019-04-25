"""

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""


class Solution(object):
    def countPrimes(self, n):
        if n <= 2:
            return 0
        # Creating the list which will help us to count prime numbers
        # we can populate it with 1,1,1,1,1
        # or True, True, True, ...
        res = [1] * n
        print(res)
        # first two numbers from range (0 and 1) are not the prime numbers
        # and we will not include them in the further calculations
        res[0] = res[1] = 0
        print(res)
        for i in range(2, n):
            print('i: ',i)
            # here we are checking only the numbers where
            # in the check list we have 1
            if res[i] == 1:
                print('here we will check the numbers in range('
                      '{}, ({}-1)/ {} + 1), which is equal {}/{}'.format(
                    i,n,i,n-1,i+1
                ))
                for j in range(i, (n - 1) // i + 1):
                    print('j: ', j)
                    res[i * j] = 0
                    print('we will zero the following element in check array',i*j)
                    print(res)
        return sum(res)

solution = Solution()
print(solution.countPrimes(10))
    # another version which works but too long for leetcode
    # def countPrimes(self, n):
    #     if n < 2:
    #         return 0
    #     count = [1] * n
    #     print(count)
    #     count[0] = count[1] = 0
    #     print(count)
    #     for i in range(n):
    #         print(i)
    #         if count[i] == 1:
    #             check = 1
    #             for j in range(2, i):
    #                 if (i % j) == 0:
    #                     print(i, "is not a prime number")
    #                     print(j, "times", i // j, "is", i)
    #                     check = 0
    #                     count[i] = 0
    #                     break
    #             if check!=0:
    #                 print('{} is prime number'.format(i))
    #                 count[i] = 1
    #                 print(count)
    #
    #     return sum(count)


    # this one works, but it is too slow
    # def countPrimes(self, n):
    #     count = 0
    #     for i in range(n):
    #         if i > 1:
    #             check = 1
    #             for j in range(2, i):
    #                 if (i % j) == 0:
    #                     print(i, "is not a prime number")
    #                     print(j, "times", i // j, "is", i)
    #                     check = 0
    #                     break
    #             if check!=0:
    #                 count+=1
    #
    #     return count
    # def countPrimes(self, n):
    #     count = 0
    #     for i in range(n):
    #         print('i: ', i)
    #         for j in range(i):
    #             print('-----j: ', j)
    #             if j % 2 == 0 and j > 0:
    #                 print('-------{}%2=0'.format(j))
    #                 count += 1
    #                 break
    #
    #
    #     print(count)




    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     if n <=1:
    #         return 0
    #     if n == 2:
    #         return 1
    #     prime_count = 0
    #     got_prime = False
    #     for i in range(n):
    #         print('checking: ',i)
    #         if i <= 1:
    #             prime_count = prime_count
    #         if i == 2:
    #             print('got 2')
    #             prime_count += 1
    #             print("prime_count: ", prime_count)
    #         for j in range(2, i+1):
    #             print('checking in second loop: ', j)
    #             if j % 2 == 0:
    #                 got_prime = False
    #             else:
    #                 got_prime = True
    #                 print('got the prime: ', j)
    #         if got_prime:
    #             prime_count += 1
    #             print("prime_count: ", prime_count)
    #
    #     return prime_count

        # def countPrimes(self, n):
        #     """
        #     :type n: int
        #     :rtype: int
        #     """
        #     count_primes = 0
        #     check = [0] * n
        #
        #     i = 2
        #     while i < n:
        #         print('i: ', i)
        #         if check[i] == 0:
        #             print('check[i]: ', check[i])
        #             count_primes += 1
        #             for j in range(i, n, i):
        #                 print('j: ', j)
        #                 check[j] = 1
        #                 print('check[j]: ', check[j])
        #                 print(check)
        #         i += 1
        #     return count_primes

    # def countPrimeshelper(self, n):
    #     if n > 1:
    #
    #         for i in range(2, n):
    #             if (n % i) == 0:
    #                 print(n, "is not a prime number")
    #                 print(i, "times", n // i, "is", n)
    #                 return False
    #         else:
    #             print(n, "is a prime number")
    #             return True
    #
    #     else:
    #         print(n, "is not a prime number")
    #
    # def countPrimes(self, n):
    #     count = 0
    #     for i in range(n):
    #         if solution.countPrimeshelper(i):
    #             count+=1
    #     return count




