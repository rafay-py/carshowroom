from models.showroom import Showroom
from models.car import Car
from models.employee import Employee
from models.customer import Customer
from datetime import datetime

showroom1 = Showroom("CS Motors", "ABC Road")

print("=== Welcome to CS Motors ===")

while True:
    print("\n=== Main Menu ===")
    print("1. Admin")
    print("2. Employee")
    print("3. Customer")
    print("0. Exit")

    role = input("Choose your role (0-3): ").strip()

    if role == '0':
        print("Exiting CS Motors...")
        break

    elif role == '1':
        # Admin Menu
        while True:
            print("\n=== Admin Menu ===")
            print("1. Manage Cars")
            print("2. Manage Employees")
            print("3. Manage Customers")
            print("4. Display Sales")
            print("5. View Total Revenue")
            print("0. Back to Main Menu")

            choice = input("Enter your choice (0-5): ").strip()

            if choice == '0':
                break

            elif choice == '1':
                # Car management
                while True:
                    print("\n=== Car Management ===")
                    print("1. Add Car")
                    print("2. View All Cars")
                    print("3. Search Cars")
                    print("4. Update Car Price")
                    print("5. Remove Car")
                    print("0. Back to Main Menu")

                    car_choice = input("Enter your choice (0-5): ").strip()

                    if car_choice == '0':
                        break
                    
                    elif car_choice == '1':
                        car_id = showroom1.generate_car_id()
                        print(f"Car ID for this car is {car_id}.")

                        car_brand = input("Enter the car brand: ").strip()
                        car_color = input("Enter color: ").strip()

                        while True:
                            try:
                                car_year = int(input("Enter car year: "))
                                if car_year <= 0:
                                    print("Year must be positive.")
                                    continue
                                break
                            except ValueError:
                                print("Please enter a valid whole number.")

                        car_condition = input("Enter car condition (New or Used): ").strip().capitalize()

                        while car_condition not in ("New", "Used"):
                            print("Please enter New or Used.")
                            car_condition = input("Enter car condition (New or Used): ").strip().capitalize()

                        car_model = input("Enter model: ").strip()
                        car_transmission = input("Enter car's transmission (Automatic or Manual): ").strip().capitalize()
                        while car_transmission not in ("Automatic", "Manual"):
                            print("Please enter Automatic or Manual.")
                            car_transmission = input("Enter car transmission (Automatic or Manual): ").strip().capitalize()
                        
                        car_fueltype = input("Enter car's fuel type: ").strip()

                        while True:
                            try:
                                car_mileage = int(input("Enter mileage of the car: "))
                                if car_mileage < 0:
                                    print("Mileage cannot be negative.")
                                    continue
                                break
                            except ValueError:
                                print("Please enter a valid whole number.")

                        while True:
                            try:
                                car_price = int(input("Enter car price: "))
                                if car_price <= 0:
                                    print("Price must be greater than zero.")
                                    continue
                                break
                            except ValueError:
                                print("Please enter a valid whole number.")

                        car = Car(
                            car_id,
                            car_brand,
                            car_color,
                            car_year,
                            "Available",
                            car_condition,
                            car_model,
                            car_transmission,
                            car_fueltype,
                            car_price,
                            car_mileage
                        )

                        showroom1.add_car(car)
                        print("Car added successfully.")

                    elif car_choice == '2':
                        showroom1.display_cars()

                    elif car_choice == '3':
                        brand = input("Enter the brand name you want to search: ").strip()
                        car_result = showroom1.search_cars(brand)
                        if not car_result:
                            print("No cars found matching that brand.")
                        else:
                            for car in car_result:
                                car.display_details()
                                print("-" * 20)

                    elif car_choice == '4':
                        while True:
                            car_id_input = input("Enter the car ID to update it's price: ").strip()
                            if not car_id_input.isdigit():
                                print("Please enter the correct numeric ID.")
                                continue
                            car_id_to_update = int(car_id_input)

                            try:
                                new_price = int(input("Enter new price of the car: "))
                                if new_price <= 0:
                                    print("Price must be greater than zero.")
                                    continue
                                showroom1.update_price(car_id_to_update, new_price)
                                break
                            except ValueError:
                                print("Please enter a valid whole number.")

                    elif car_choice == '5':
                        remove_carid = input("Enter the car id to remove: ").strip()
                        if remove_carid.isdigit():
                            showroom1.remove_car(int(remove_carid))
                        else:
                            print("Invalid car ID.")

                    else:
                        print("Invalid input! Try again.")

            elif choice == '2':
                # Employee Management
                while True:
                    print("\n=== Employee Management ===")
                    print("1. Add Employee")
                    print("2. View All Employees")
                    print("3. Search Employees")
                    print("4. Update salary")
                    print("5. Remove Employee")
                    print("0. Back to Main Menu")

                    employee_choice = input("Enter your choice (0-5): ").strip()

                    if employee_choice == '0':
                        print("Exiting...")
                        break

                    elif employee_choice == '1':
                        employee_id = showroom1.generate_employee_id()
                        print(f"ID for this employee is {employee_id}.")

                        employee_name = input("Enter your full name here: ").strip().capitalize()
                        employee_email = input("Enter your email: ").strip()
                        hire_date = datetime.now()
                        while True:
                            try:
                                employee_contact = int(input("Enter employee contact number: "))
                                break
                            except ValueError:
                                print("Please enter a valid phone number!")

                        employee_role = input("Enter the role of the employee (Staff or Admin): ").strip().capitalize()
                        while employee_role not in ("Staff", "Admin"):
                            print("Please enter Staff or Admin.")
                            employee_role = input("Enter the role of the employee (Staff or Admin): ").strip().capitalize()

                        while True:
                            try:
                                employee_salary = int(input("Enter the designated salary of the employee: "))
                                if employee_salary <= 0:
                                    print("Salary must be greater than zero.")
                                    continue
                                break
                            except ValueError:
                                print("Please enter a valid whole number.")

                        employee = Employee(
                            employee_id,
                            employee_name,
                            employee_contact,
                            employee_email,
                            hire_date,
                            employee_role,
                            employee_salary
                        )
                        showroom1.add_employee(employee)
                        print(f"Employee with employee id {employee_id} added successfully.")

                    elif employee_choice == '2':
                        print("\n=== Employees ===")
                        showroom1.display_employees()

                    elif employee_choice == '3':
                        emp_name = input("Enter the full name of the employee you want to search: ").strip().capitalize()
                        emp_result = showroom1.search_employee(emp_name)
                        if not emp_result:
                            print("No employees found matching that name.")
                        else:
                            for emp in emp_result:
                                emp.display_details()
                                print("-" * 20)

                    elif employee_choice == '4':
                        while True:
                            emp_id_input = input("Enter the Employee ID to update their salary: ").strip()
                            if not emp_id_input.isdigit():
                                print("Please enter the correct numeric ID.")
                                continue
                            emp_id_to_update = int(emp_id_input)

                            try:
                                new_salary = int(input("Enter new salary of the employee: "))
                                if new_salary <= 0:
                                    print("Salary must be greater than zero.")
                                    continue
                                showroom1.update_salary(emp_id_to_update, new_salary)
                                break
                            except ValueError:
                                print("Please enter a valid whole number.")

                    elif employee_choice == '5':
                        remove_emp_id = input("Enter the ID of the employee to remove: ").strip()
                        if remove_emp_id.isdigit():
                            showroom1.remove_employee(int(remove_emp_id))
                        else:
                            print("Invalid employee ID.")

                    else:
                        print("Invalid input! Try again.")

            elif choice == '3':
                # Customer Management
                while True:
                    print("\n=== Customer Management ===")
                    print("1. Register a Customer")
                    print("2. Search Customer")
                    print("3. Display Customer")
                    print("0. Back to Main Menu")

                    customer_choice = input("Enter your choice (0-3): ").strip()

                    if customer_choice == '0':
                        print("Exiting...")
                        break

                    elif customer_choice == '1':
                        customer_id = showroom1.generate_customer_id()
                        print(f"ID for this customer is {customer_id}")

                        customer_name = input("Enter full name of the customer: ").strip().capitalize()
                        customer_email = input("Enter the customer's email: ").strip()
                        city = input("Enter city of the customer: ").strip().capitalize()
                        address = input("Enter the residential address of the customer: ").strip()
                        registration_date = datetime.now()
                        while True:
                            try:
                                customer_contact = int(input("Enter customer contact number: "))
                                break
                            except ValueError:
                                print("Please enter a valid phone number!")

                        customer = Customer(
                            customer_id,
                            customer_name,
                            customer_contact,
                            customer_email,
                            city,
                            address,
                            registration_date
                        )

                        showroom1.add_customer(customer)
                        print(f"{customer_name} added as a customer successfully.")

                    elif customer_choice == '2':
                        cust_name = input("Enter the full name of customer to search: ").strip().capitalize()
                        cust_result = showroom1.search_customer(cust_name)
                        if not cust_result:
                            print("No customers found matching that name.")
                        else:
                            for cust in cust_result:
                                cust.display_details()
                                print("-" * 20)

                    elif customer_choice == '3':
                        print("===\n Customers ===")
                        showroom1.display_customers()

                    else:
                        print("Invalid choice! Try again please.")

            elif choice == '4':
                print("\n=== Sales ===")
                showroom1.display_sales()

            elif choice == '5':
                total_revenue = showroom1.calculate_revenue()
                print(
                    f"Total showroom revenue: "
                    f"{total_revenue:,.2f} PKR"
                )

            else:
                print("Invalid input! Try again.")

    elif role == '2':
        # Employee Menu
        while True:
            print("\n=== Employee Menu ===")
            print("1. View Available Cars")
            print("2. Search Cars")
            print("3. Record Sale")
            print("0. Back to Main Menu")

            choice = input("Enter your choice (0-3): ").strip()

            if choice == '0':
                print("Exiting...")
                break

            elif choice == '1':
                print("\n=== Cars ===")
                showroom1.display_cars(filter_status="Available")

            elif choice == '2':
                car_name = input("Enter car brand to search for: ").strip().capitalize()
                car_result = showroom1.search_cars(car_name)
                if not car_result:
                    print("No cars found matching that brand.")
                else:
                    for car in car_result:
                        car.display_details()
                        print("-" * 20)
                
            elif choice == '3':
                car_id_input = input("Enter the car ID of the car to sell: ").strip()
                buying_customer_input = input("Enter the customer id: ").strip()
                selling_employee_input = input("Enter your ID: ").strip()

                if not (car_id_input.isdigit() and buying_customer_input.isdigit() and selling_employee_input.isdigit()):
                    print("Car ID, Customer ID, and Employee ID must all be numeric!")
                    continue

                car_id_to_buy = int(car_id_input)
                buying_customer_id = int(buying_customer_input)
                selling_employee_id = int(selling_employee_input)

                payment_method = input("Enter payment method: ").strip().capitalize()

                discount_input = input("Enter discount in PKR (If the discount is zero simply press '0'): ").strip()
                if "%" in discount_input:
                    print("Please enter discount with a fixed price.")
                    continue
                try:
                    discount = int(discount_input)
                except ValueError:
                    print("Please enter a valid discount input! Try again.")
                    continue

                try:
                    while True:
                        sale_price = int(input("Enter sale price of the car: "))
                        if sale_price <= 0:
                            print("Price must be valid and above zero.")
                            continue
                        break
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                print("Making the sale...")
                initial_sales_count = len(showroom1.sales)
                showroom1.record_sale(car_id_to_buy, buying_customer_id, selling_employee_id, sale_price, payment_method, discount)

                # Check if sale was recorded successfully
                if len(showroom1.sales) > initial_sales_count:
                    print("Sale made successfully!")
                    print(f'''Car with ID {car_id_to_buy} 
is sold to customer with ID {buying_customer_id} 
by employee {selling_employee_id} on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} 
with total price {sale_price - discount} PKR''')

            else:
                print("Invalid input! Try again.")

    elif role == '3':
        # Customer Menu
        while True:
            print("\n=== Customer Menu ===")
            print("1. View Available Cars")
            print("2. Search Cars")
            print("0. Back to Main Menu")

            choice = input("Enter your choice (0-2): ").strip()

            if choice == '0':
                print("Exiting...")
                break

            elif choice == '1':
                print("\n=== Cars ===")
                showroom1.display_cars(filter_status="Available")

            elif choice == '2':
                car_name = input("Enter car brand to search for: ").strip().capitalize()
                car_result = showroom1.search_cars(car_name)
                if not car_result:
                    print("No cars found matching that brand.")
                else:
                    for car in car_result:
                        car.display_details()
                        print("-" * 20)
                
            else:
                print("Invalid input! Try again.")

    else:
        print("Invalid input! Please choose 0, 1, 2, or 3.")