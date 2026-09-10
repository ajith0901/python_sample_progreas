"""
def function name(parameters):
    code to be executed 
"""
"""    
#function whithout parameters
def welcome():
    print("welcome ajith")

welcome() 
welcome()   

#function whith parameter
def greeting(username,userage):
    print(f"welcome {username},you are {userage} yers old")

greeting("ajith",24)    
"""
"""
def addition(num1,num2):
    return num1+num2

num1=int(input("Enter the first number: "))    
num2=int(input("Enter the second number: ")) 
print(addition(num1,num2))

#positional arguments
def book_ticket(moviename,customername,seat,ticketprice):
    totalprice=seat*ticketprice
    return f"{customername} booked {seat} ticket for {moviename}. total amount : {totalprice}"
print(book_ticket("vas","ajin",2,300))

#keyword arguments
def customer_details(customername,customerage,customercity):
    print(f"{customername} is {customerage} yers old.{customername} live in {customercity}")
customer_details(customerage=24,customername="aji",customercity="marthandam") 
"""
"""
#default arguments
def booking_status(customername="aji",status="conformed",screen="screen1"):
    print (f"{customername} is booking status is {status}. the screen allocated is {screen}")   
booking_status()
booking_status("ajith")    
booking_status("kumar","pending")
"""
"""
#multiple arguments

def calulate_bill(*ticketprice):
    print(f"ticketprice : {ticketprice}")

calulate_bill(150,200,300,500,550)    
"""
"""
#try out kwarts

#built in function

print(len("aji"))
print(sum([1,2,3,4]))
print(min([1,2,3,4]))
print(max([1,2,3,4]))
print(sorted([5,6,7,8]))
print(sorted([5,6,7,8],reverse=True))

#legb rule

def student_details():
    name="aji"
    print("student name: ",name)
student_details()
print("student name: ",name)  

#globel veriables

college_name="maria college"
def display():
    print("college name: ",college_name)
display()   

#enclosing variable

def department():
    department_name="cse"
    def student():
        print("department name: ",department_name)
    student()
department()  

"""
"""
tax=50 #globel vaeiable
def shopping():
    discount=100 #enclosing variable
    def bill():
        amount=1000
        total_amount=amount-discount+tax
        print("total amount is: ",total_amount)
    bill()
shopping()       

#recursive function
def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)
num=int(input("enter a number: "))   
print(factorial(num))  

#working 
6*factorial(5)
6*5*factorial(4)
6*5*4*factorial(3)
6*5*4*3*factorial(2)
6*5*4*3*2*factorial(1)
"""
"""

#lambda function
#lambda arguments:expression syntex

def add(num1,num2):
    return num1+num2
print(add(3,6))              

add=lambda a,b:a+b
print(add(5,6))

square=lambda num:num*num
print(square(7))
"""
celsius_to_f=lambda c:(c*9/5)+32
print(celsius_to_f(50))

multiply=lambda a,b:a*b
print(multiply(7,8))

cube=lambda a:a**3
print(cube(3))

is_odd=lambda a:a%2!=0
print(is_odd(7))

smallest=lambda a,b,c:min(a,b,c)
print(smallest(8,7,2))

area=lambda l,b:l*b
print(area(20,30))
