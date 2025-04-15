class Vehicle:
    def move(self):
        pass
#Car
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")
#Plane
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")
#Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

for vehicle in (Vehicle(), Car(), Plane(), Boat()):
    vehicle.move()  # Calls the move method of each class