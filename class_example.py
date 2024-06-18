class Dog:
    def __init__(self, name, breed, color):
        self.name = name
        self.breed = breed
        self.color = color 

    def bark(self):
        return f"{self.name} screams because hes a {self.breed}!"
    
#  Class always capital letter
my_dog = Dog("Odin", "Husky", "Black and white")
neighbors_dog = Dog("Pepper", "Bordercollie", "Black and grey")
# Fetching the attributes of the class using objects
print(my_dog.name)

print(my_dog.bark())

print(neighbors_dog.bark())

