#object - is an entity having state behaviour and identity
#eg- pen-->identity -- its name,state --colour, brand, model, behaviour--write,draw
#class is a group of similer object or its an user defined datatype

#4 Basics principles or poillars of oops
#1 inheritance
#2 ploymorphism
#3 abstraction
#4 encapsulation
"""
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


#next class object initialization
class car:
    colour="black"
    colour2="white"
    def __init__(self,brand,model):  #instance variable :variable inside function
        self.brand=brand
        self.model=model
car_object=car("bmw","m5")        
print(car_object.brand,car_object.model,car_object.colour)
#print(car_object.model)
car_object=car("mercedez","amg")
print(car_object.brand,car_object.model,car_object.colour2)

class Library:
    def __init__(self,book,author):
        self.book=book
        self.author=author
    def book_count(self,count):
        self.count=count    
lib_object=Library("little women","mary")
print(lib_object.book,lib_object.author)
lib_object.book_count(2)  
print(lib_object.count) 

#1.inheritance : 
#1.single level inheritance 

class user:  #base class or parent class or super class
    def login(self):
        print("user logged in")
class Ifluencer(user):  #childe class/sub class/derived class
    def postreels(self):
        print("influencer posted anew reel")  
inf_object=Ifluencer()
inf_object.postreels()
inf_object.login()     

#multilevel inheritance
class vehicle:
    def category(self,mode):
        print("mode of transport: ",mode)
class car(vehicle):
    def vehicle_category(self,vehicle_type,colour):
        print("type of vehicle: ",vehicle_type)
        print("colour of vehicle: ",colour)      
class Electriccar(car):
    def car_type(self,brand,category,variant,price):
        print(f" vehicle brand is {brand} and the category is {category}.its variant is {variant} having price {price}") 
ecar=Electriccar()
ecar.category("road")
ecar.vehicle_category("car","blue")
ecar.car_type("audi","electric","r8","5 crores")        

#multiple inheritance
class ImageUpload:
    def Uploadimage(self,username,imagename):
        print(f"{username} posted {imagename} successfully")
class ReelUpload:
    def Uploadreels(self,reel_tittle,reel_duration):
        print(f"uploaded reel is {reel_tittle} of {reel_duration} seconds")
class Instagram(ImageUpload,ReelUpload):
        def user_analytics(self,user_name,owner,reaction):
            print(f"{user_name} is having a {owner} account with {reaction} reaction on post uploaded")
insta=Instagram()
insta.Uploadimage("ajith","flower")
insta.Uploadreels("flower_reel","15")
insta.user_analytics("ajith","meta","10000")    
"""
"""
#hybrid and hierarchical

class Vehicle:
    def category(self,mode):
        print("mode of transport: ",mode)
class Car(Vehicle):
    def car_model(self,model):
        print("car model is: ",model)
class Bike(Vehicle):
    def bike_model(self,model):
        print("bike model is: ",model) 
class Sportsvehicle(Car,Bike):
    def vehicle_range(self,range):
        print("vehicle range is: ",range)

vehicle=Vehicle()
vehicle.category("road")
car=Car()
car.car_model("bmw")
bike=Bike()
bike.bike_model("KTM")
sp_vehicle=Sportsvehicle()
sp_vehicle.vehicle_range(200)

# hierarchical

class Vehicle:
    def type(self):
        print("vehicle type is fuel")
class car(Vehicle):
    def car_model(self):
        print("car is sports model")  
class bike(Vehicle):   
    def bike_model(self):
        print("bike is sports model")
class jeep(Vehicle):
    def jeep_model(self):
        print("jeep is sports model") 

vehicle=Vehicle()
vehicle.type()

car=car()
car.type()
car.car_model()
bike=bike()
bike.type()
bike.bike_model()
jeep=jeep()
jeep.type()
jeep.jeep_model()

class Account:
    def details(self):
        print("account details")
class Loan:
    def datails(self):
        print("loan details")        
class Customer(Account,Loan):
    def datails(self):
        print("customer details")
        super().details() #MRO method resolution  order
customer=Customer()
customer.details()   


#ploymorphism-reperecenting single object in many ways
#method over loading - same class same method difference arrguments.eg facebook loging
#method over riding - differnce class same method same parameter. account loging in difference class

class Calculatore:
    def sum(self,num1=0,num2=0,num3=0):
        return num1+num2+num3
calculatore=Calculatore()
result=calculatore.sum(15,20)
print(result)

class Facebook:
    def loging(self,email=None,password=None,phonenumber=None):
        if email and password:
            print(f"loging throuh email id: {email}")
        elif phonenumber and password:
            print(f"loging throuh mobile number: {phonenumber}")    
        else:
            print("invalid loging")    

facebook=Facebook()
facebook.loging(email="ajith@gamil",password=12345)
facebook.loging(phonenumber=7894561230,password=123456)  

#method over loading
#payment process cash upi card

class Payment:
    def method(self,cash=None,upi=None,card=None):
        if cash:
            print(f"cash payment is: {cash}")
        elif upi:
            print(f"UPI payment is: {upi}")
        elif card:
            print(f"Card payment is: {card}")
        else:
            print("invalid payment method")     
payment=Payment()
payment.method(cash=500)
payment.method(upi=400)
payment.method(card=700)

class Payment:
    def method(self,cash=None,upi=None,card=None):
        if cash or card:
            print(f"cash payment is: {cash}, card payment {card}")
        elif card or upi:
            print(f"card payment {card}. UPI payment is: {upi}")
        else:
            print("invalid payment method")     
payment=Payment()

payment.method(upi=400)


#method over riding

class Employee:
    def work(self):
        print("working as employee")
class Manager(Employee):
    def work(self):
         print("managing team") 
         super().work() 
manager=Manager()  
manager.work()           


#3.abstraction -hiding the implementation details from the user .eg atm widhrawal

from abc import ABC,abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod    
    def stop_engine(self):
        pass 

class Car(Vehicle):
    def start_engine(self):
        print("car started using key")
    def stop_engine(self):
        print("car stopped using key")   

car_object=Car()
car_object.start_engine()
car_object.stop_engine()  
#vehicle_obje=Vehicle()     #conot instantiat abstract class VEHICLE. cnnot creat object when class is abstract.(ABC)             
#if a class abstract all the absrtact method must be implement in its child class

#Encapsulation-data hiding mechanism    
class Persion(): 
    def __init__(self,name,age):
        self.name=name
        self.__age=age  # __private variable

    def show_age(self):    #public method
        print(self.__age)

    def get_age(self):
        return self.__age

    def set_age(self,age):
        if age>0:
            self.__age
        else:
            print("age must be positive")          

persion_obj=Persion("ajith",24)
print(persion_obj.name)
#print(persion_obj.age)  #cnnot access as a outsid the class as its a private variable
persion_obj.show_age()

persion_obj.set_age(25)
print(persion_obj.get_age())
#updation of value setter(),getter() we can access it for reading and writing 


#duck typing if an object behaves the requird object python doesnot care about its actual class.
#duck typing
class PDF:
    def print_document(self):
        print("printing pdf")
class Word:  
    def print_document(self):
        print("printing word")
def print_file(file):
    file.print_document()

pdf_obj=PDF()
word=Word()
print_file(word)      #print file function dosenot check whether object is pdf or word it only check whether has print doucument    

#composition - one class contain object of another class(has a relationship)

class Engine:
    def start(self):
        print("engine started")
class Car:
    def __init__(self):
        self.engine=Engine()  

    def start_car(self):
        self.engine.start()
        print("car stared") 
car=Car()
car.start_car()               
"""

#name mangling -internal data hiding 

class BankAccount:
    def __init__(self,balance):
        self.__balance=balance

    def show_balance(self):
        print("balance: ",self.__balance) 

bankaccount=BankAccount(500) 
bankaccount.show_balance()      





