# question 19- Write an 'Employee' class including the following methods and print the final salary

class Employee:
    def __init__(self, name, hours, salary):
        self.name = name
        self.hours = hours
        self.salary = salary

    def getName(self):
        print(self.name)

    def setName(self):
        self.name = str(input("Enter new name: "))
        print(self.name)

    def getWorkHours(self):
        print(self.hours)

    def setWorkHours(self):
        self.hours = int(input("Enter new hours weekly: "))
        while self.hours > 48:
            self.hours = int(input("Cannot require more than 48 hours. Enter new hours weekly: "))
        print(self.hours)

    def getSalaryRate(self):
        print(self.salary)

    def setSalaryRate(self):
        self.salary = float(input("Enter new hourly salary rate: "))
        while self.salary < 15:
            self.salary = float(input("Cannot be below $15. Enter new hourly salary rate: "))
        print(self.salary)

    def __add




Employee1 = Employee("John", 40, 40)
Employee2 = Employee("Aaya", 48, 52)

Employee1.getName()
Employee1.setName()
Employee1.getWorkHours()
Employee1.setWorkHours()
Employee1.getSalaryRate()
Employee1.setSalaryRate()