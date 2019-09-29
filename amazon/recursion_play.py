"""
write a function to retreive all the letters in the list
as long as it has some and if there is no letters left
tell about it

"""

def say_letter(array):
    if len(array) < 1:
        print("Horray no leters left")
        return
    print(array[0])
    return say_letter(array[1:])



"""
write a recursive function to calculate
sum of the values in the list
"""

def summ_elements(array):
    if len(array)<1:
        return 0
    return array[0] + summ_elements(array[1:])


"""
write a function to calculate fibanachi number
"""

def calc_fib(number):
    if number < 1:
        return 1
    else:
        return calc_fib(number -1) + calc_fib(number-2)

"""
write the function for fibona4i num
but use nor recursive and iteration
"""

def fib_iter(n):
    a,b = 0,1

    if n == 1:
        print(a)

    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a + b
            a = b
            b = c
            print(c)



##############################################

# say_letter(['a', 'b','c','d','e',])
# print(summ_elements([1,2,3,4,5]))
# print(calc_fib(5))
print(fib_iter(10))