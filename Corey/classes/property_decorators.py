# https://www.youtube.com/watch?v=jCzT9XFZ5bw

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@company.com'

    # this @property allows us use our email method as a attribute
    # and when we invoke it do not add () like email()
    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)


    # we can use the same here and transform the full_name method to the attribute
    # using the same @property decorator
    @property
    def full_name(self):
        return "{} {}".format(self.first, self.last)

    # now we want to create the setter method which should allow
    # us to set the full name and at the same time change the first
    # and last name from that property

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # here we are going to create the deleter decorator

    @full_name.deleter
    def full_name(self):
        print('Deleting name')
        self.first = None
        self.last = None

emp1 = Employee('John', 'Smith')

emp1.first = "Jim"

# print(emp1.full_name())
# now when we have the full_name with the @property decorator in the class
# we can use it like the usual attribute and not add ()
print(emp1.full_name)
print(emp1.first)
print(emp1.last)
# in such case we need to add () to the end of the email because now it is
# method and not the property
# print(emp1.email())
print(emp1.email)

print()
emp1.full_name = 'Boris Strugatskiy'

print(emp1.full_name)
print(emp1.first)
print(emp1.last)
print(emp1.email)

print()
del emp1.full_name
print(emp1.full_name)