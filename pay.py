# python program to implement a payroll system

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_payroll(self):
        raise NotImplementedError("Subclasses must implement this method")
# creating salary employee class, a child class of employee class
class SalaryEmployee( Employee):
    def __init__(self, emp_id, name, weekly_salary):
        super().__init__(emp_id, name)
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary

# creating hourly employee class, a child class of employee class
class HourlyEmployee( Employee):
    def __init__(self, emp_id, name, hours_worked, hourly_rate):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hourly_rate

# creating commission employee class, a child class of salaryemployee class
class CommissionEmployee(SalaryEmployee):
    def __init__(self, emp_id, name, weekly_salary, commission):
        super().__init__(emp_id, name, weekly_salary)
        self.commission = commission

    def calculate_payroll(self):
        return self.weekly_salary + self.commission

def main():
    # Create employees
    emp1 = SalaryEmployee(1, "David", 1500)
    emp2 = HourlyEmployee(2, "Wafula", 40, 20)
    emp3 = CommissionEmployee(3, "Soita", 1000, 500)

    # List of employees
    employees = [emp1, emp2, emp3]

    # Process payroll
    for emp in employees:
        print(f"Payroll for {emp.name} (ID: {emp.emp_id}): ${emp.calculate_payroll():.2f}")

if __name__ == "__main__":
    main()
