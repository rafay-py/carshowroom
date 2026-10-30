from datetime import datetime

class Customer():
    def __init__(self, customer_id, name, phone_number, email, city, address, registration_date):
        self.__customer_id = customer_id # private
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.city = city
        self.address = address
        self.registration_date = registration_date

    @property
    def customer_id(self):
        return self.__customer_id

    def get_details(self):
        return {
            "Name" : self.name,
            "City" : self.city,
            "Address" : self.address,
            "Email" : self.email,
            "Contact" : self.phone_number,
            "Registration date" : self.registration_date
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
            "customer_id": self.customer_id,
            "name": self.name,
            "phone_number": self.phone_number,
            "email": self.email,
            "city": self.city,
            "address": self.address,
            "registration_date": self.registration_date.isoformat() if isinstance(self.registration_date, datetime) else self.registration_date
        }

        