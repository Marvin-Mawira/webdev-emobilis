# Define a class called "Person"
class Person:
    # Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to introduce the person
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Create instances (objects) of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes and call methods on objects
person1.introduce()
person2.introduce()

# Modify attributes
person1.age = 31

# Check the updated age
person1.introduce()
