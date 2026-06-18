class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, employee_id, name, department):
        if employee_id in self.employees:
            raise ValueError("Employee ID already exists")

        self.employees[employee_id] = {
            "id": employee_id,
            "name": name,
            "department": department,
        }

        return self.employees[employee_id]

    def find_employee(self, employee_id):
        return self.employees.get(employee_id)

    def list_employees(self):
        return list(self.employees.values())


if __name__ == "__main__":
    manager = EmployeeManager()
    manager.add_employee(1, "Anirudhan", "HR")
    manager.add_employee(2, "Barath", "Engineering")

    for employee in manager.list_employees():
        print(employee)