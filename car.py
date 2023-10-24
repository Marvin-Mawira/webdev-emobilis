class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            print(f"The {self.year} {self.make} {self.model} is starting.")
            self.is_running = True
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            print(f"The {self.year} {self.make} {self.model} is stopping.")
            self.is_running = False
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

# Create instances of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car("Ford", "Focus", 2021)

# Interact with the Car objects
car1.start()
car2.start()
car1.stop()
car2.stop()
