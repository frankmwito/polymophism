# Polymorphism with Duck Typing
# In Python, we can use duck typing to achieve polymorphism. Duck typing is a concept where
# the suitability of an object is determined by the presence of certain methods or properties,
# rather than the actual type of the object. This means that we can write code that works with
# objects of different classes, as long as they have the required methods or properties.

class Person:
    def move(self):
        print("Walking on two legs")
        
class Robot:
    def move(self):
        print("Rolling on wheels")
        
def start_moving(entity):
    # Polymorphism with duck typing: Both Person and Robot have a move() method
    entity.move()

# Create instances of Person and Robot
person = Person()
robot = Robot()

# Test the function with both objects
start_moving(person)  # Should print "Walking on two legs"
start_moving(robot)   # Should print "Rolling on wheels"


