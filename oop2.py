class students:
    def __int__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age


    def display(self):
        print("Name: %s \nCourse: %s \nGender: %s \nAge: %d"
        %(self.name, self.course, self.gender, self.age))

students1 = students("BIT", "Female", 30)
students2 = students("Bob", "CS", "Male", 25)