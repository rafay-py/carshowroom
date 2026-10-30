from datetime import datetime

class Sales():
    def __init__(self, sale_id, car_id, customer_id, employee_id, sale_date, sale_price, discount, payment_method):
        self.__sale_id = sale_id # private
        self.car_id = car_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.sale_date = sale_date
        self.sale_price = sale_price
        self.discount = discount
        self.payment_method = payment_method

    @property
    def sale_id(self):
        return self.__sale_id

    def get_details(self):
        return {
            "Car ID" : self.car_id,
            "Customer ID" : self.customer_id,
            "Employee ID" : self.employee_id,
            "Date of sale" : self.sale_date,
            "Sale price" : self.sale_price,
            "Discount" : self.discount,
            "Payment method" : self.payment_method
        }

    def display_details(self):
        details = self.get_details()

        for key, value in details.items():
            print(f"{key} : {value}")

    def calculate_final_amount(self):
        return self.sale_price - self.discount

    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "car_id": self.car_id,
            "customer_id": self.customer_id,
            "employee_id": self.employee_id,
            "sale_date": self.sale_date.isoformat() if isinstance(self.sale_date, datetime) else self.sale_date,
            "sale_price": self.sale_price,
            "discount": self.discount,
            "payment_method": self.payment_method
        }