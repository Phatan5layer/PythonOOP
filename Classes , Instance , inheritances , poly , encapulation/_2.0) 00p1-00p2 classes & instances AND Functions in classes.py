'''

Some definitions are incomplete like c-method and method

ez sequence to remember first

1)class
class Attributes
2)Constructor
Constructor Attributes (but they are also called instance attributes)
3)Instance Methods
Instance Attributes
4)Instances
5)print stuff


1- Class: A blueprint for creating objects.
-Class Attributes: Shared properties for all instances.

2- Constructor: Initializes object attributes when an instance is created.
-Constructor Attributes (Instance Attributes)*: Instance-specific properties.

3-Instance Methods: Functions that work with instance attributes.
-Instance Attributes: Properties specific to each instance, defining their characteristics or state

4-Instances: Individual objects created from the class with their own attributes.

5-Print Stuff: Actions performed on instances or their attributes.


-------------------------------------------------------------------------

Proper sequence to know how it starts
(added constructor method and method )
(anything covered with [] is e.g code after || )

 -Class                      ||  [class BluePrint:]
    = Class Attributes       ||  shared properties of blueprint                            ||
 -Constructor Method       ||  [ (def __init__ (self ,stuff ,stuff2) ]
   = Instance Attributes   ||  [ self.something = something ]
   = Instance Attributes


 -Method                   ||  [ def something(self) ]
   = Instance Attributes   ||  properties that a method can access
   = Instance Attributes

:Instances                  ||  [example = BluePrint]
:Instances(from methods)    ||  [example = Method]

print etc

-------------------------------------------------------------------------


So, the sequence can be defined as follows:

-1)Class:
The blueprint or template for creating objects.
-1a)Class Attribute:
A property associated with the class itself (shared among instances).

-2)Constructor :
The initialization instructions for crafting a new object from class
-2a)Constructor attribute

-3)Instance Method
A specialized action that an object, created from the class, is capable of performing.
-3a)Instance Attribute:
One individual object made from the blueprint (class), which has its own unique features.

4)Instance :
A feature that belongs to a specific object created from  blueprint(class).

5)print (end)

'''



#-using () are instances (objects created from classes).


#-using [] are lists which is a way to group items together in Python
 #(data structures for collections of items).

#-method refers to a function that is associated with an
# object or a class (check below code)
#-result = MyObject.MyMethod()


# object "se" is defined as = software engineer

'''
lets say if we have loads of se from se1-se5 , it will become
cumbersome which could be lead to either errors , mistakes , confusion
or missing data , which is why we use "classes"


#E.g of This is alot of work without using classes
#position , name , age , level , wage
se1 = ["umer" , "96" , "junior" , "$10"]
se2 = ["khan" , "3" , "CEO" , "$20,000"]
se3
se4
se5
etc
imagine having se in 100s But you want a specific type(s) of data

===================================================

or another example
se1 = ("SE1", "umer", "20", "$4")
se2 = ("SE2", "khan", "90", "$20,000")
d1 = ["designer", "ali"]

def code(se):
    print(f"{se[1]} is writing code...")

code(d1)
code(se1)
code(se2)
------------------------------------
#Answer
designer is writing code...
SE1 is writing code...
SE2 is writing code...
-----------------------------------

very conusing

'''


#is se1 & se2 are instances?
'''
#se1 and se2 are not instances . They are actually lists containing
 information about individuals who might be software engineers.
 They're surrounded by [] not ()
'''


#why do we use class?
'''
In python we have primitive data structures like integers and
strings or lists ,but they are designed to represent only
simple pieces of information
what happens if we want to have a more complex type of data that
we want to represent so in this example
let's use a software engineer as a class later below
'''


#what are classes?
'''
Think of a class as a blueprint which something needs to be defined
We first give the name like this with the keyword "class"
Then we give an instances 
'''

#class is the blueprint or template.
#SoftwareEngineer is the name of the blueprint
'''
class SoftwareEngineer:
    pass # The pass statement inside the class is like saying,
         # "There's nothing specific to write here yet."
'''




#what are class attributes
'''
A class attribute in Python is like a shared piece of information among 
all the objects created from a class.

Imagine you have a group of friends, and you all share a favorite color. 
That favorite color is like a class attribute. If one person changes the favorite color, 
it changes for everyone because you all share the same favorite color.
'''




#Now we are coding the real deal with SE name , age , level , wage

#-it will involve a class , class attribute and
#  instance and instance attribute

class SoftwareEngineer:  #Blueprint for a SoftwareEngineer

    #class attribute
    nickname = "phatan"

#-Below is  "constructor method"
#-The '__init__' method is the special "constructor method"
# (used to initialize instances of the 'SoftwareEngineer' class.)
    def __init__(self, name , age , level , wage):

    # instances attributes stored inside the "SoftwareEngineer" class
        self.name = name
        self.age = age
        self.level = level
        self.wage = wage
    # instance attributes like name are tied to a specific instance
    # class attribute is same for every instance

    #Below is instance Method
    def cod_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")


#Below stuff are instacnes of the class
#Creating instances (software engineers) from the class.
se1 = SoftwareEngineer("umer" , "96" , "junior" , "$4")
se2 = SoftwareEngineer("khan" , "3" , "CEO" , "$20,000")


print(se1.wage , se2.name , )
#-Access class attribute , weather directly from class attribute
# or from instance
print(se2.nickname)
print(SoftwareEngineer.nickname)
se1.cod_in_language("python in japanese") #calling method (se1)
se2.cod_in_language("meow") #calling method(se2)



'''
================================================================================
================================================================================
================================================================================
================================================================================
================================================================================
'''
#Now the code is without the comments for more clairty

print("")

class SoftwareEngineer:
    nickname = "phatan"

    def __init__(self, name, age, level, wage):
        self.name = name
        self.age = age
        self.level = level
        self.wage = wage

    def cod_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    def information(self): #extra part in this code
        information = f"name = {self.name}, age = {self.age}, level = {self.level} (extra stuff)"
        return information

se1 = SoftwareEngineer("umer", "96", "junior", "$4")
se2 = SoftwareEngineer("khan", "3", "CEO", "$20,000")


print(se1.wage, se2.name)
print(se2.nickname)
print(SoftwareEngineer.nickname)
se1.cod_in_language("python in japanese")
se2.cod_in_language("meow")
print(se1.information())
print(se2.information())

