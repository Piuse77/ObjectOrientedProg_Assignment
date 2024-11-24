class Smartphone:
    def __init__(self, brand, model, price, battery_level=100):
        # Constructor to initialize the smartphone's attributes
        self.brand = brand
        self.model = model
        self.price = price
        self.battery_level = battery_level
    
    def make_call(self, phone_number):
        # Simulates making a phone call
        if self.battery_level > 0:
            print(f"Calling {phone_number}... 📞")
            self.battery_level -= 5  # Battery decreases with each call
        else:
            print("Battery is too low to make a call! Please charge your phone.")
    
    def charge_battery(self):
        # Charges the phone's battery
        self.battery_level = 100
        print("Charging complete! Battery is now at 100%. 🔋")
    
    def get_info(self):
        # Displays the smartphone's information
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Battery: {self.battery_level}%"

# Create an instance of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 14", 999.99)

# Test the methods
print(my_phone.get_info())  # Display smartphone info
my_phone.make_call("555-1234")  # Make a call
my_phone.charge_battery()  # Charge the phone


#QUESTION TWO

class Vehicle:
    def move(self):
        # A general move method for all vehicles
        pass

class Car(Vehicle):
    def move(self):
        # Car's version of the move method
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        # Plane's version of the move method
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        # Boat's version of the move method
        print("Sailing ⛵")

# Create instances of each vehicle
car = Car()
plane = Plane()
boat = Boat()

# Polymorphism in action
vehicles = [car, plane, boat]

for vehicle in vehicles:
    vehicle.move()  # Each vehicle calls its own move() method
