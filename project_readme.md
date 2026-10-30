# Car Showroom Management System

A multi-tier terminal-based Car Showroom Management System built in Python using Object-Oriented Programming (OOP) principles and JSON file persistence.

This project simulates real-world showroom operations by supporting three distinct user roles (**Admin**, **Employee**, and **Customer**), allowing users to manage inventory, track staff records, register customers, and log completed sales.

---

## 🌟 Key Features

* **Role-Based Access Control:**
  * **Admin:** Full system control—add/remove cars, update vehicle pricing, manage employees and salary records, register customers, view sales records, and calculate total showroom revenue.
  * **Employee:** View inventory status, search vehicles by brand, and process car sales with automated ID validation and custom discount calculations.
  * **Customer:** Browse available cars and search inventory by brand.
* **Persistent Data Storage:** Automatic JSON serialization (`showroom_data.json`) saves state changes instantly and reloads records seamlessly when restarting the app.
* **Data Validation & Protection:** Safe user inputs with `try-except` blocks, status checks ("Available", "Sold", "Reserved"), and read-only attributes (using `@property` getters) for unique entity IDs.

---

## 🏗️ Project Architecture & OOP Concepts

The project adheres to key Object-Oriented Programming principles and clean modular design:

```
carshowroom/
│
├── main.py                    # Entry point & interactive CLI menu loop
└── models/
    ├── car.py                 # Car class with attribute encapsulation
    ├── customer.py            # Customer class with contact update methods
    ├── employee.py            # Base Employee class with Admin & Staff subclasses
    ├── sales.py               # Sales transaction logic and discount calculation
    └── showroom.py            # Main Manager class handling state, CRUD, & JSON storage
```

* **Encapsulation:** Internal identifiers (`car_id`, `customer_id`, `sale_id`) are protected as private attributes (`__id`) with public getter properties.
* **Inheritance:** `Admin` and `Staff` sub-classes inherit common attributes and behaviors from the base `Employee` class.
* **Composition:** The central `Showroom` class maintains and coordinates collections (`cars`, `customers`, `employees`, and `sales`).
* **Serialization / Deserialization:** Converts complex Python objects into JSON-friendly dictionaries (`to_dict()`) and reconstructs them upon app initialization.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your system.

### Running the Application

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/car-showroom-management.git
   cd car-showroom-management
   ```

2. **Launch the app:**
   ```bash
   python main.py
   ```

3. **Navigate the menu:**
   Follow the interactive command-line prompts to switch roles (Admin, Employee, or Customer) and test out the showroom features!

---

## 💡 Tech Stack

* **Language:** Python 3
* **Libraries Used:** Standard built-in modules (`json`, `os`, `datetime`)

---

## 📝 Learning Outcomes

Building this project helped reinforce foundational software development skills:
* Designing modular file structures in Python.
* Applying core OOP concepts (Encapsulation, Inheritance, Composition).
* Implementing JSON File I/O for data persistence across application runs.
* Structuring interactive terminal menus with robust validation and error handling.