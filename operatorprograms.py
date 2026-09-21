"""
1 arithmetic operator
2 assingment operator
3 logical
4 comparision
5 bitwaise
6 membership
7 identity 


print("arithmetic operator")
price_per_phone=20000
quantity=5
total_price=price_per_phone*quantity
average_price=total_price/quantity
gst_added=200
final_price=total_price+gst_added
discount_amount=1000
final_price=final_price-discount_amount
number_of_persion=3
remaining_price=final_price%number_of_persion
floor_division=final_price//7

print("price per phone is: ",price_per_phone)
print("quantity is: ",quantity)
print("total price: ",total_price)
print("average price is: ",average_price)
print("gst price is: ",gst_added)
print("discount amount of phone is: ",discount_amount)
print("final price of all phone: ",final_price)
print("floor division is: ",floor_division)


#Assignment operators
score=100
score+=50
score-=20
score*=3
print(score)

#logical operator
and-both condittion must be true
or-any of the condision must be true
not-oppsite of the condition 

username="ajith"
password="12345"
entered_username=input("Enter the username: ")
entered_password=input("Enter the password: ")
if username==entered_username and password==entered_password:
    print("logged in succesfully")
else:
    print("invalid login")    

#or operator
day=input("Enter a day")
if day=="saturday" or day=="sunday":
    print("holiday")
else: 
    print("working day")

#not
logged_in=False
if not logged_in:
    print("loggin successful, welcom user")
else:
    print("please login") 

#membership operators 
#checks whether an element is present or not keywods

#in
movies=["harry potter","kill bill","train"]
movie=input("enter a movie")
if movie in movies:
    print("movie available")
else:
    print("movie is not available")  

#not in    

employees=["aji","abi","kumar"]
employe_name=input("Enter the employee name")
if employe_name not in employees:
    print("access denied")
else:
    print("access granded")  
"""
#identity operators checks whether memory location is same or not
#key wods is or not
valu1=35
valu2=35
print(valu1 is valu2)
print(valu1==valu2)

list1=[35,34,33]
list2=[35,34,33]
print(list1 is list2)
print(list1==list2) 

#bitwise operators
a=5
b=3
print(a & b)
#0 1 0 1
#0 0 1 1
#0 0 0 1 
print(a | b)
#0 1 0 1
#0 0 1 1
#0 1 1 1
print(a ^ b) #x or
#0 1 0 1
#0 0 1 1
#0 1 1 0

print(~a) #-a+1

print(5<<1) #5*2^1
print(5<<2)

print(5>>1) #5/2^1
print(5>>2)

