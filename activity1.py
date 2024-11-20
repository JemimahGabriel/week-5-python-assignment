# Base class: Animal
class Animal:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} the {self.species} says: {self.sound}")

# Subclass: Dog
class Dog(Animal):
    def __init__(self, name, breed, sound="Woof"):
        super().__init__(name, "Dog", sound)
        self.breed = breed

    def fetch(self):
        print(f"{self.name} is fetching the ball!")

# Subclass: Cat
class Cat(Animal):
    def __init__(self, name, color, sound="Meow"):
        super().__init__(name, "Cat", sound)
        self.color = color

    def scratch(self):
        print(f"{self.name} the {self.color} cat is scratching the furniture!")

# Instantiate objects
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "Black")

# Use methods
dog.make_sound()
dog.fetch()

cat.make_sound()
cat.scratch()
