class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def Countemployee(self):
        Employee.empCount +=1

    def set_name(self, name):
        self.name = name

    def set_salary(self, salary):
        self.__salary = salary


b=Employee("Mandar",45000)
print(b.empCount)
print(b.name)
print(b.salary)

class Manager(Employee):
    pass


