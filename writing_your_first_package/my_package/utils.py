
class Customer:
    def __init__(self):
        self.name = None

    def set_name(self, name):
        self.name = name

    def identity(self):

        print("I'm a Customer " + self.name)

    def we_need_to_talk(self, break_up=False):
        """
        Helper for communication with significant other
        :param break_up: bool
        :return: None
        """
        if break_up:
            print(f"{self.name}, it's not you, it's me...")
        else:
            print(f"I <3 U, {self.name}!")


class MyCounter:

    def set_count(self, n):
        self.count = n


# Include a set_name method
class Employee:
    def __init__(self):
        self.salary = None
        self.name = None

    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary

    def give_raise(self, amount):
        self.salary = self.salary + amount

    # Add monthly_salary method that returns 1/12th of salary attribute
    def monthly_salary(self):
        return self.salary / 12


customer = Customer()
customer.set_name("Laura")
customer.identity()
customer.we_need_to_talk(break_up=True)

mc = MyCounter()
mc.set_count(5)
mc.count = mc.count + 1
print(mc.count)


emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)
# Get monthly salary of emp and assign to mon_sal
mon_sal = emp.monthly_salary()
# Print mon_sal
print(mon_sal)
