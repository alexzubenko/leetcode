class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_employees +=1

    def full_name(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amnt(cls, amount):
        cls.raise_amount = amount

    # this is the alternative constructor so we can parse the
    # input string to create the new employee
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


    # instead of passing the instance of the class (self) or class itself (cls)
    # static method does not pass anything automatically, so in other words they
    # behave like regular functions, but have some logical connection with the class
    # where they created
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



# print(Employee.num_of_employees)

empl_1 = Employee('bob', 'bruth', 900000)
empl_2 = Employee('mona', 'tereet', 100000)


# empl_1.first = "Bob"
# empl_1.lase = "Guru"
# empl_1.email = "bob@guru.com"
# empl_1.pay = 200000
#
#
# empl_2.first = "Bob2"
# empl_2.lase = "Guru2"
# empl_2.email = "bob2@guru2.com"
# empl_2.pay = 220000



# print(empl_1.email)
# print(empl_2.email)
#

# print(Employee.full_name(empl_1))
# print(empl_1.full_name())

# Employee.raise_amount = 1.99
# empl_1.raise_amount = 2
# print(empl_1.pay)
# empl_1.apply_raise()
# print(empl_1.pay)




# print(Employee.__dict__)
# print()
# print(empl_1.__dict__)

# print(Employee.num_of_employees)

# Employee.set_raise_amnt(1.09)
#
#
#
# print(Employee.raise_amount)
# print(empl_1.raise_amount)
# print(empl_2.raise_amount)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Alice-Bort-80000'
emp_str_3 = 'Jane-Cobu-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

import datetime

my_date = datetime.date(2017, 7, 10)

print(Employee.is_workday(my_date))