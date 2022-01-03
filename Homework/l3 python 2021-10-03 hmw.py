import random
# Q15- Write a class named Rectangle constructed (means constructor) by a length and width and a method which will
# compute the area of a rectangle. Create two different Rectangle objects and print out areas

class rectangle:
    def __init__(self, length = 100, width = 20):
        self.length = length
        self.width = width

    def set_length(self):
        self.length = float(input("Please enter length: "))
        while self.length <= 0:
            self.length = float(input("Cannot be less than or equal to 0. Please enter length: "))
        return self.length

    def set_width(self):
        self.width = float(input("Please enter width: "))
        while self.width <= 0:
            self.width = float(input("Cannot be less than or equal to 0. Please enter length: "))
        return self.width

    def get_area(self):
        area = self.length * self.width
        return area


# question 19- Write an 'Employee' class including the following methods and print the final salary
class Employee:
    list_of_ids = [1, 2, 3, 4, 5, 6]
    unique_id = random.choice(list_of_ids)
    list_of_ids.remove(unique_id)

    def __init__(self, name = "employee"+str(unique_id), hours = 40, salary = 15):
        self.name = name
        self.hours = hours
        self.salary = salary

    def get_name(self):
        print(self.name)

    def set_name(self):
        self.name = str(input("Enter new name: "))
        print(self.name)

    def get_work_hours(self):
        print(self.hours)

    def set_work_hours(self):
        self.hours = int(input("Enter new hours weekly: "))
        while self.hours > 48:
            self.hours = int(input("Cannot require more than 48 hours. Enter new hours weekly: "))
        print(self.hours)

    def get_salary_rate(self):
        print(self.salary)

    def set_salary_rate(self):
        self.salary = float(input("Enter new hourly salary rate: "))
        while self.salary < 15:
            self.salary = float(input("Cannot be below $15. Enter new hourly salary rate: "))
        print(self.salary)

    def __add_subsidy__(self):
        if self.salary < 500:
            return 10
        else:
            print("Over $500 salary.")

    def __add_overtime__(self):
        if self.hours > 40:
            overtime = self.hours - 40
            total = overtime * self.salary * 2
            return total

    def get_salary(self):
        print("At the end of", self.name, "'s week, they earned: ")
        print((self.hours * self.salary) + self.__add_overtime__() + self.__add_subsidy__())



Rectangle1 = rectangle()
print(Rectangle1.get_area())

Employee1 = Employee()
Employee2 = Employee()
Employee3 = Employee()

Employee1.get_name()
Employee1.set_name()
Employee1.get_work_hours()
Employee1.set_work_hours()
Employee1.get_salary_rate()
Employee1.set_salary_rate()
Employee1.get_salary()


print(Employee1.unique_id)
print(Employee2.unique_id)
print(Employee3.unique_id)



