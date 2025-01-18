class Human:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def show_passengers(self):
        if self.passengers:
            print(f"{self.brand} passengers:")
            for pas in self.passengers:
                print(pas.name)
        else:
            print("No passengers")

jack = Human("Jack")
bob = Human("bob")
nik = Human("nik")

car1 = Car("Mercedes")

car1.add_passenger(jack)
car1.add_passenger(bob)
car1.add_passenger(nik)


car1.show_passengers()
