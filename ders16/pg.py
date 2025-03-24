class Employee:
    def __init__(self, name, salary, position) :
        self.name = name
        self.salary = salary
        self.position = position

    def get_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.05

class Manager(Employee):
    def __init__(self, name, salary, position, team_size):
        super().__init__(name, salary, position)
        self.team_size = team_size

    def get_details(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

    def calculate_bonus(self):
        return self.salary * 0.10




employee = Employee("John Doe", 50000, "Developer")
manager = Manager("Jane Smith", 80000, "Project Manager", 10)

employee_bonus = employee.calculate_bonus()
employee.get_details()
print(f"Bonus: {employee_bonus}")

manager_bonus = manager.calculate_bonus()

manager.get_details()
print(f"Bonus: {manager_bonus}")