class animal:
    def speaks(self):
        print("animal speaks")

class cat(animal):
    def meows(self):
        print("cat meows")

paka = cat()
paka = meows()


print(animal_sound(cat))  # Outputs: "Meow!"