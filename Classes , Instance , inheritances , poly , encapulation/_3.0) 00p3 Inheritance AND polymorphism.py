
'''

Topics covered

-Inheritances ( done )
-expand ( done )  (check se child class for .fixcode )
-override ( done ) (check se child class for .level)

-polymorphism , (check end of this page)

'''




#Inheritance meaning
'''

-Inheritance is the process in which one class takes on
 the attributes and methods of the another class
-The newly formed class is called a childs class
 and the other one is called the parents class(os ka baap)

'''

#pc = parent class
#cm = Constructor method
#ca = Constructor attribute
#im = instance method
#ia = instance attribute

#se SoftwareEngineer
#de = Designer


#We can override this
class Employee: #parent class = pc (please remember this)

    def __init__(self, name , age , salary): #cm
        self.name = name #ca
        self.age = age
        self.salary = salary

    def work(self):#this (.work) in both part of de and se /#im
        print(f"{self.name} is hustling, (Part of em, check pc)")#check print statement

# ---------------------------------------------------------


# child class attributes inherited from pc , which is name , age , salary
# .level is not from pc , rather a seperate attribute
class SoftEngineer(Employee):#child class / im
    '''
-se has the __init__ function because we wanted to
 add an extra attribute called level
-de inherits the __init__  from em so it has the same 
 attributes as em unless we define additional ones
    ''' #why se has __init__ and not de
    def __init__(self, name, age, salary, level):
        '''

-In order to get the (contructor)attributes from the class/pc 
 we call the __init__(constructor method) from its pc by
 writing it as "" supper().__init__(stuff from pc , etc ) ""
-Its either called superfunction or "superclass constructor call"


-We wont write the already written constructor attributes from pc like
    self.name = name
    self.age = age
    self.salary= salary

-But we can write { self.level = level } [ since its not part of pc if
 we want to extend some stuff and will only work for se ]

   {
#like this

        super().__init__(name ,age)
        self.level = level

    }

        '''  # big comment about super()
        super().__init__(name, age, salary)
        self.level = level  # not from pc but seperate attribute of se

    def fixbug(self):#im
        print(f"{self.name} is fixing bug (only part of se)")#check print statement



# child class attributes inherited from pc , which is name , age , salary
class Designer(Employee):  # child class attributes inherited from pc

    def draw(self):#im
        print(f"{self.name} is drawing (only part of de)")#check print statement

# ===========================================================

#.............

print("")

# printing (name , age , salary , work)
em = Employee("(1)Name: employer", "9 years" , "$1,000,000")

print(em.name, em.age, em.salary)
em.work()#defined in pc

print("")  # above is baseClass/pc

#.............


# printing (name , age , salary , work ), level , fixbug
# another level in seperate line)
se = SoftEngineer("(2)Name: UMER", "19 years" , "$10,000" , ", senior j")

print(se.name, se.age, se.salary , se.level)
print(se.level)#we can also print level like this
se.work()  #from base class/pe(which isnt in the childs class)
se.fixbug() #only part of se
print("")  # above is childs class se

#.............


# printing (name , age , salary , work) , draw
de = Designer("(3)Name:KhAn ", "39" , "$2500")

print(de.name, de.age, de.salary)
de.work()  #from base class/pe(which isnt in the childs class)
de.draw()  #onlt part of de

print("")  # above is childs class de

#.............

#===========================================================


#seperate but same code below
'''
class Employee:
    def __init__(self, name , age , salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is hustling, (Part of em, check pc)")

class SoftEngineer(Employee):
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def fixbug(self):
        print(f"{self.name} is fixing bug (only part of se)")

class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing (only part of de)")



print("")


em = Employee("(1)Name: employer", "9 years" , "$1,000,000")
print(em.name, em.age, em.salary)
em.work()


print("")  


se = SoftEngineer("(2)Name: UMER", "19 years" , "$10,000" , ", senior j")
print(se.name, se.age, se.salary , se.level)
print(se.level)
se.work()
se.fixbug()


print("")  


de = Designer("(3)Name:KhAn ", "39" , "$2500")
print(de.name, de.age, de.salary)
de.work()
de.draw()


print("")  


'''



print("========================================================")



#Polymorphism
'''

-An object have different types of behaviour

-Example code in Language
-language is the same object being used repeatedly but
 is used differently or the value changes each time it's used
 
'''

def say_hello(language):
    if language == "arabic":
        return "salam"
    elif language == "russian":
        return "vodka"
    elif language == "german":
        return "hans gets ze flammenwerfer"
    else:
        return "yo"

print(f"Arabic: {say_hello('arabic')}")
print(f"Russian: {say_hello('russian')}")
print(f"German: {say_hello('german')}")
print(f"Default: {say_hello('english')}")


