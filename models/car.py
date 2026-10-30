class Car:
    def __init__(self, car_id, brand, color, year, status, condition, model, transmission, fuel_type, price, mileage):
        self.__car_id = car_id # private attribute
        self.brand = brand
        self.color = color
        self.year = year
        self.status = status
        self.condition = condition
        self.model = model
        self.transmission = transmission
        self.fuel_type = fuel_type
        self.price = price
        self.mileage = mileage

    
    @property
    def car_id(self):
        return self.__car_id

    def get_details(self):
        return {
            "Car ID" : self.car_id,
            "Brand": self.brand,
            "Model": self.model,
            "Year": self.year,
            "Color": self.color,
            "Transmission": self.transmission,
            "Fuel Type": self.fuel_type,
            "Condition" : self.condition,
            "Mileage": self.mileage,
            "Price": self.price,
            "Status": self.status
        }

    def display_details(self):
        details = self.get_details()

        for key, value in details.items():
            print(f"{key}: {value}")

    def change_status(self, new_status):
        new_status = new_status.strip()
        if new_status.lower() not in ("available", "sold", "reserved"):
            print("Wrong status entered!")
        else:
            self.status = new_status.capitalize()

    def to_dict(self):
        return {
            "car_id": self.car_id,
            "brand": self.brand,
            "color": self.color,
            "year": self.year,
            "status": self.status,
            "condition": self.condition,
            "model": self.model,
            "transmission": self.transmission,
            "fuel_type": self.fuel_type,
            "price": self.price,
            "mileage": self.mileage
        }
