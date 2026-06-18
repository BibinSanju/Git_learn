import pytest
from app import EmployeeManager


def test_add_employee_success():
    manager = EmployeeManager()

    employee = manager.add_employee(1, "Alice", "HR")

    assert employee["id"] == 1
    assert employee["name"] == "Alice"
    assert employee["department"] == "HR"


def test_find_employee():
    manager = EmployeeManager()
    manager.add_employee(1, "Alice", "HR")

    employee = manager.find_employee(1)

    assert employee["name"] == "Alice"


def test_list_employees():
    manager = EmployeeManager()
    manager.add_employee(1, "Alice", "HR")
    manager.add_employee(2, "Bob", "Engineering")

    employees = manager.list_employees()

    assert len(employees) == 2


def test_duplicate_employee_id_rejected():
    manager = EmployeeManager()
    manager.add_employee(1, "Alice", "HR")

    with pytest.raises(ValueError):
        manager.add_employee(1, "Alice Again", "Finance")