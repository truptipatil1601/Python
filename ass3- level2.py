# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Child class
class Truck(Vehicle):
    def __init__(self, brand, model, load_capacity):
        super().__init__(brand, model)
        self.load_capacity = load_capacity

    # Overriding method
    def display_info(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Load Capacity:", self.load_capacity, "kg")


# Creating object
t1 = Truck("Tata", "Prima", 20000)
t1.display_info()
