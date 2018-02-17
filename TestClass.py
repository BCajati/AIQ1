class Employee(object):

    def __init__(self, role, salary):
        self.role = role
        self.salary = salary

    def is_contract_emp(self):
        return self.salary <= 1250

    def is_regular_emp(self):
        return self.salary > 1250


emp = Employee('Tester', 2000)

if emp.is_contract_emp():
    print("I'm a contract employee.")
elif emp.is_regular_emp():
    print("I'm a regular employee.")

print("Happy reading Python coding tips!")