#object - is an entity having state behaviour and identity
#eg- pen-->identity -- its name,state --colour, brand, model, behaviour--write,draw
#class is a group of similer object or its an user defined datatype

#4 Basics principles or poillars of oops
#1 inheritance
#2 ploymorphism
#3 abstraction
#4 encapsulation

class Student:
    def display(self):
        print("I am a student")
student_object=Student()      #object creation 
student_object.display() 

#constructer is a special method in python
#mainly used for initialising an object
#it will be autometicaly called when an object is created

class Employee:
    def __init__(self):
        print("default constructor is called")
employee=Employee()    











