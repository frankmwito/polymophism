# Polymorphic class with inheritance
class Animal:
    def __init__(self, name):
        self.name = name
        
    def speak(self):
        pass  # Abstract method to be overridden
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
    
class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"
    
def animal_sound():
    animal1 = Dog("Hercules")
    animal2 = Cat("Myles")
    animal3 = Cow("Manny")
    
    print(animal1.speak())  # Call the speak method and print the result
    print(animal2.speak())
    print(animal3.speak())

# Call the function to test
animal_sound()
