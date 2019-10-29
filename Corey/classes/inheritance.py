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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.full_name())

dev_1 = Employee('bob', 'bruth', 900000)
dev_2 = Employee('mona', 'tereet', 100000)
dev_3 = Developer('Mort', 'Morteef', 900000, 'Java')

# print(help(Developer))

# print(dev_1.email)
# print(dev_2.email)
# print(dev_3.email)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

print()
print(dev_3.pay)
dev_3.apply_raise()
print(dev_3.pay)

print(dev_3.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 9000000, [dev_1])
mgr_1.add_emp(dev_2)
mgr_1.add_emp(dev_3)

print(mgr_1.email)
mgr_1.print_emps()

print()
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print()
print(issubclass(Manager,Employee))