from models.sales import Sales
from models.car import Car
from models.customer import Customer
from models.employee import Employee
from datetime import datetime

import json
import os

class Showroom():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.cars = []
        self.customers = []
        self.employees = []
        self.sales = []

        self.load_data()

    def save_data(self):
        data = {
            "cars": [car.to_dict() for car in self.cars],
            "customers": [cust.to_dict() for cust in self.customers],
            "employees": [emp.to_dict() for emp in self.employees],
            "sales": [sale.to_dict() for sale in self.sales]
        }

        with open("showroom_data.json", "w") as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if not os.path.exists("showroom_data.json"):
            return # No saved file yet

        with open("showroom_data.json", "r") as file:
            data = json.load(file)

        # Cars
        for car_dict in data.get("cars", []):
            car = Car(
                car_dict["car_id"], car_dict["brand"], car_dict["color"],
                car_dict["year"], car_dict["status"], car_dict["condition"],
                car_dict["model"], car_dict["transmission"], car_dict["fuel_type"],
                car_dict["price"], car_dict["mileage"]
            )
            self.cars.append(car)

        # Customers
        for cust_dict in data.get("customers", []):
            reg_date = datetime.fromisoformat(cust_dict["registration_date"]) if cust_dict["registration_date"] else datetime.now()
            customer = Customer(
                cust_dict["customer_id"], cust_dict["name"], cust_dict["phone_number"],
                cust_dict["email"], cust_dict["city"], cust_dict["address"], reg_date
            )
            self.customers.append(customer)
            
        # Employees
        for emp_dict in data.get("employees", []):
            hire_d = datetime.fromisoformat(emp_dict["hire_date"]) if emp_dict["hire_date"] else datetime.now()
            employee = Employee(
                emp_dict["employee_id"], emp_dict["name"], emp_dict["phone_number"],
                emp_dict["email"], hire_d, emp_dict["role"], emp_dict["salary"]
            )
            self.employees.append(employee)
            
        # Sales
        for sale_dict in data.get("sales", []):
            sale_d = datetime.fromisoformat(sale_dict["sale_date"]) if sale_dict["sale_date"] else datetime.now()
            sale = Sales(
                sale_dict["sale_id"], sale_dict["car_id"], sale_dict["customer_id"],
                sale_dict["employee_id"], sale_d, sale_dict["sale_price"],
                sale_dict["discount"], sale_dict["payment_method"]
            )
            self.sales.append(sale)
            
        print("Previous showroom data loaded successfully!")

# Car management
    def generate_car_id(self):
        if not self.cars:
            return 1000

        highest_id = max(car.car_id for car in self.cars)
        return highest_id + 1
    
    def add_car(self, car):
        for existing_car in self.cars:
            if existing_car.car_id == car.car_id:
                print("A car with the same car ID already exists.")
                return

        self.cars.append(car)
        self.save_data()

    def remove_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id:
                self.cars.remove(car)
                print("Car removed successfully")
                return

        print("Car not found!")
        self.save_data()

    def update_price(self, car_id, new_price):
        for car in self.cars:
            if car.car_id == car_id:
                car.price = new_price
                print(f"Car with car ID {car_id} updated to new price {new_price} PKR.")
                return
            
        print("Car ID doesn't exist.")
        self.save_data()
        

    def search_cars(self, brand):
        results = []

        for car in self.cars:
            if car.brand.lower() == brand.lower():
                results.append(car)

        return results

    def display_cars(self, filter_status=None):
        if not self.cars:
            print("No cars record available.")
            return

        cars_to_show = self.cars
        if filter_status:
            cars_to_show = [car for car in self.cars if car.status == filter_status]

        if not cars_to_show:
            print(f"No cars found with status {filter_status}.")
            return

        for car in cars_to_show:
            car.display_details()
            print("-" * 20)

# Customer management
    def generate_customer_id(self):
        return len(self.customers) + 1000
    
    def add_customer(self, customer):
        for existing_customer in self.customers:
            if existing_customer.customer_id == customer.customer_id:
                print("A customer with the same ID already exists.")
                return

        self.customers.append(customer)
        self.save_data()

    def search_customer(self, name):
        results = []

        for customer in self.customers:
            if customer.name.lower() == name.lower():
                results.append(customer)

        return results

    def display_customers(self):
        if not self.customers:
            print("No customers record available.")
            return

        for customer in self.customers:
            customer.display_details()

# Employee management
    def generate_employee_id(self):
        if not self.employees:
            return 1000

        highest_id = max(employee.employee_id for employee in self.employees)
        return highest_id + 1

    def add_employee(self, employee):
        for existing_employee in self.employees:
            if existing_employee.employee_id == employee.employee_id:
                print("An employee with the same ID already exists.")
                return

        self.employees.append(employee)
        self.save_data()

    def remove_employee(self, employee_id):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                self.employees.remove(employee)
                print("Employee removed successfully.")
                return

        print("Employee not found!")
        self.save_data()

    def search_employee(self, name):
        results = []

        for employee in self.employees:
            if employee.name.lower() == name.lower():
                results.append(employee)

        return results

    def update_salary(self, employee_id, new_salary):
        for employee in self.employees:
            if employee.employee_id == employee_id:
                employee.salary = new_salary
                print(f"{employee.name} with employee ID {employee_id} got their salary updated to {new_salary} PKR.")
                return
            
        print("Employee ID doesn't exist.")
        self.save_data()


    def display_employees(self):
        if not self.employees:
            print("No employees record available.")
            return

        for employee in self.employees:
            employee.display_details()
    
# Sales management
    def generate_sale_id(self):
        sale_id = len(self.sales) + 1000
        return sale_id
    
    def record_sale(self, car_id, customer_id, employee_id, sale_price, payment_method, discount):
        car_found = False
        car_available = False
        found_car = None
        for existing_car in self.cars:
            if existing_car.car_id == car_id:
                car_found = True
                found_car = existing_car
                print("Car exists in the inventory. Finding car status...")
                if existing_car.status.lower() == "available":
                    car_available = True
                    print("Car is available. Ready for sale.")
                else:
                    print("Car is already sold or reserved.")

        if not car_found:
            print("Car not found!")

        employee_found = False
        for existing_employee in self.employees:
            if existing_employee.employee_id == employee_id:
                employee_found = True
                print("Employee ID validated. Proceeding further...")

        if not employee_found:
            print("Employee not found!")

        customer_found = False
        for existing_customer in self.customers:
            if existing_customer.customer_id == customer_id:
                customer_found = True
                print("Customer ID recorded correctly...")

        if not customer_found:
            print("Customer not registered!")

        if not car_found or not car_available or not employee_found or not customer_found:
            return

        else:
            sale_id = self.generate_sale_id()
            sale = Sales(sale_id, car_id, customer_id, employee_id, datetime.now(), sale_price, discount, payment_method)
            self.sales.append(sale)
            found_car.change_status("Sold")
            self.save_data()


    def calculate_revenue(self):
        if not self.sales:
            return 0
        revenue = 0
        for sale in self.sales:
            revenue += sale.calculate_final_amount()

        return revenue

    def display_sales(self):
        if not self.sales:
            print("No sales record available.")
            return

        for sale in self.sales:
            sale.display_details()
