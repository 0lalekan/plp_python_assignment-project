# Assignment 1
class Smartphone:
    def __init__(self, brand, model, storage, price):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__price = price  # private attribute

    def specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB"
    
    def get_price(self):
        return f"Price: ${self.__price}"
    
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price. Price must be positive.")


# inheritance (child class)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, ram, refresh_rate, price):
        super().__init__(brand, model, storage, price)   # inherit from parent class
        self.ram = ram
        self.refresh_rate = refresh_rate

    # polymorphism - method overriding
    def specs(self): 
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, RAM: {self.ram}GB, Refresh Rate: {self.refresh_rate}Hz"
    


# Create objects
phone1 = Smartphone("Apple", "iPhone 13", 128, 999)
phone2 = GamingPhone("Samsung", "Galaxy S24 Ultra", 256, 12, 120, 1299)

# Demonstrate OOP concepts
print(phone1.specs())          # Abstraction
print(phone1.get_price())      # Encapsulation

print(phone2.specs())          # Polymorphism (overridden method)
print(f"Old Price: {phone2.get_price()}")      # Encapsulation
phone2.set_price(1199)         
print(f"Discounted Price: {phone2.get_price()}")      # Updated price



# Assignment 2 -   Polymorphism with different classes
class Car:
    def move(self):
        return "The car is driving"

class Boat:
    def move(self):
        return "The boat is sailing"

class Plane:
    def move(self):
        return "The plane is flying"
# Create objects
car = Car()
boat = Boat()
plane = Plane()


print(car.move())
print(boat.move())
print(plane.move())

# OR create object

def vehicle_move(vehicle):
    print(vehicle.move())

vehicle_move(car)
vehicle_move(boat)
vehicle_move(plane)


# OR create a list of objects
vehicles = [car, boat, plane]
for v in vehicles:
    print(v.move())



        