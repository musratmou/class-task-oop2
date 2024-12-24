class SalaryNotInRange(Exception):
    def __init__(self, message="Salary must be between 10000 and 50000"):
        self.message = message
        super().__init__(self.message)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_salary(self):
        if self.salary < 10000 or self.salary > 50000:
            raise SalaryNotInRange(f"Invalid salary: {self.salary}. Salary must be between 10000 and 50000.")
        else:
            print(f"Employee Name: {self.name}")
            print(f"Salary: {self.salary}")

# Example usage
try:
    employee = Employee("John Doe", 60000)
    employee.display_salary()
except SalaryNotInRange as e:
    print(f"Error: {e}")
