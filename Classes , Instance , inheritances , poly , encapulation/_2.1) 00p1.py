'''
-Here's a simple code example that combines the concepts of a
 class, class attribute, instance, and instance attribute:
'''


# Class definition for a 'Dog' blueprint
class Dog:
    species = "Canine"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def bark(self):
        print(f"{self.name} says Woof!")

# Creating two 'Dog' objects (instances) with instance attributes
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 2)

# Explanation:
# - "Dog" is the class definition, acting as the blueprint for creating dog objects.
# - "species" is a class attribute shared by all instances of the "Dog" class.
# - "name" and "age" are instance attributes specific to each individual dog object.
# - "bark" is an instance method that allows each dog to perform the action of barking.

# Accessing class attribute and instance attributes
print(f"{dog1.name} is a {Dog.species}.")
print(f"{dog1.name} is {dog1.age} years old.")
dog1.bark()
print(f"{dog2.name} is {dog2.age} years old.")
dog2.bark()


'''
In this code:

We create two "Dog" objects (instances), each with its own 
"name" and "age", and then we access both class attributes and 
instance attributes for these objects. 
The "bark" method demonstrates an instance-specific behavior.
'''


