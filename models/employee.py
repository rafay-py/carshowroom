from datetime import datetime

class Employee():
    def __init__(self,employee_id, name, phone_number, email, hire_date, role, salary):
        self.employee_id = employee_id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.hire_date = hire_date
        self.role = role
        self.salary = salary

    def get_details(self):
        return {
            "Name" : self.name,
            "Employee ID": self.employee_id,
            "Contact" : self.phone_number,
            "Email" : self.email,
            "Date of hiring" : self.hire_date,
            "Role" : self.role,
            "Salary" : self.salary
        }

    def display_details(self):
        details = self.get_details()
        for key, value in details.items():
            print(f"{key} : {value}")

    def update_phone_number(self, new_phone_number):
        if not new_phone_number.isdigit():
            print("The phone number must contain digits!")
        else:
            self.phone_number = new_phone_number

    def to_dict(self):
        return {
            "employee_id": self.employee_id,
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
            "hire_date": self.hire_date.isoformat() if isinstance(self.hire_date, datetime) else self.hire_date,
            "role": self.role,
            "salary": self.salary
        }

class Admin(Employee):
    pass

class Staff(Employee):
    pass
