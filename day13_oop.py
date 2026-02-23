class Car:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def show_details(self):
        print("Brand:", self.brand)
        print("Price:", self.price)


c1 = Car("Tata", 2000000)
c2 = Car("Hyundai", 1500000)

c1.show_details()
c2.show_details()