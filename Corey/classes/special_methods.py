class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees +=1

    def __repr__(self):
        return "Employee ('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return "{} - {}".format(self.full_name(), self.email)

    # create a method that will allow to add two employees together
    # and get the total salary
    def __add__(self, other):
        return self.pay + other.pay

    # create the method to rerurn the total number of characters
    # in the employee full name
    def __len__(self):
        return len(self.first) + len(self.last)

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)




emp_1 = Employee('bob', 'bruth', 900000)
emp_2 = Employee('mona', 'tereet', 100000)

print(emp_1)

print()
print(repr(emp_1))
print(str(emp_1))

print()
print(emp_1.__repr__())
print(emp_1.__str__())

print()
print(1 + 2)

print()
print(int.__add__(1,2))
print(str.__add__('1','2'))

# testing the created dunder method to sum the two employees salaries
print(emp_1.__add__(emp_2))

print()
print(len('test'))
print('test'.__len__())

print()
print(emp_1.__len__())