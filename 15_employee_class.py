
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def setname(self, name):
        self.name = name

    def setage(self, age):
        self.age = age

    def setsalary(self, salary):
        self.salary = salary

    def __str__(self):
        return f"name={self.name}, age={self.age}, salary={self.salary}"

emp = Employee("Ahmed Ali", 20, 500)
print(emp)
