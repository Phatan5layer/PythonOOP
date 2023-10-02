'''
-Dont know which part uses 
abstraction but i know some idea of it

-Abstraction in the context of OOP is about simplifying 
complex systems by breaking them into smaller, more manageable 
parts and hiding the unnecessary details. It's like using a 
TV remote control without needing to know how the remote 
communicates with the TV internally. 
''' #abstraction

#skipped decorator

'''
Encapsulations
-It means hiding of data
-Involves hiding or protecting data within a class to maintain
 data integrity and control on how data accessed and modified.

-In this tutorial , we will use '_' and '__'
 (single and double underscores)

(1)'_variable' is called protected attribute (one underscore)
_variables are meant for internal use.
Developers should access them , and users should avoid direct access.
(2)__variable is called a private attribute(double underscore)
__variables are private. Avoid direct access, even for developers
''' #Encapsulation
print("")
#-Using same example of se

class SoftwareEnigneer:

    def __init__(self , name , age):
        self.name = name #Public attribute
        self.age = age #Public attribute
        self._bugs_fixed = 0#used "_" to make the data protected
        self.__salary = None #used "__" to make the data private

se = SoftwareEnigneer("umer" ,21 ,) # "self._bugs..." is zer0
print(se.name , se.age ,  se._bugs_fixed)#._bugs will still work
try:#code trys to print salary but wont work due to __
    print(se.__salary)#used 2 underscore
except AttributeError:#used this for clean output ,code error
    print("Cannot show salary because the parameter is using '__'")


print("")
print("===========Almost same code , but added removed(commend)code =============")
print("")

'''



-Suppose the HR department needs to have the data of salary of the 
 se , while still having the attribute with __salary 
-We will use the getter and setter functions , we will first set
the price(not print it) and then get the price(print it)

'''
#--------------------------------------------------------

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name #not used
        self.age = age #not used
        self._bugs_fixed = 0
        self.__salary = None



    ''' 
        -The above  is a Getter functions 
        it "ask" an object for its current state or value.
        ''' # below is a getter funtion
    #hr wants access the salary even with "__" ( instances methods)
    def get_salary(self):
      return self.__salary


    '''
    -The below is a Setter functions 
    it tell an object to change its state or value
    
    -In setters , i always put the value  like
    
    [
    def something(self, value):
        self.stuff = value
    ]
    
    ''' #setter
    #hr sets salary , without it , we wouldnt get_salary output
    def set_salary(self , value ):
        self.__salary = value


#--------------------------------------------------------------

se =SoftwareEngineer("Umer", 21) #instance


''' 
    =putting the try/except , & print name/age/bugs 
     code here just in case
     

print(se.name, se.age, se._bugs_fixed)#prints name and age

#hr sets salary , without it , we wouldnt get_salart output
    def set_salary(self , value):
        self.__salary = value
'''
se.set_salary(6000)#wont print anything , its only set
print(se.get_salary())


