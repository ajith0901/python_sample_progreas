"""
if condition:
    code to be executed
elif condition
    code to be executed
else:
    code to be executed

"""
"""
num=int(input("Enter a number: "))
if num>=0:
    print("positive number")
else:
    print("negative number")

vowelchecker=input("enter a charector")
if vowelchecker in "aeiouAEIOU":
    print("enterd charector is a vowel")
else:
    print("enterd charector is a consonant")   
    
 

num=int(input("enter a number"))
if num%2==0:
    print("number is even")
else:
    print("number is odd") 


#elif condition     
age=int(input("enter your age"))
if age<=13:
    print("child")
elif age<18:
    print("teenage")
elif age<60:
    print("adult")
else:
    print("senior citizen")  


#nested if
num=int(input("Enter a number: "))
if num>=0:
    if num%2==0:
        print("number is positive and even")
    else:
        print("number is positive and odd")    
else:
    print("negative number") """

#chek wether given number is 3 digit or not    
#for and while are entry controller loop

"""
for variable in sequence:
    code to be executed

#using range function
for variable in range(start,stop,step):
    code to be executed
start=default valu is 0   
stop=number -1
step=defult valu is 1 for positive number and for negative number we need to assign

#syntax for while loop:
initialization
while condition:
    code to be executed
    updation 
"""    
"""
word=input("enter a word: ")
for letter in word:
    print(letter)

for element in range(11):
    print(element)  
   

for element in range (5,15):
    print(element)    

for element in range(10,25,5):
    print(element)  
     
for item in range(10,0,-1):
    print(item)  

for item in range(17,3,-3):
    print(item) 

multiple=int(input("enter a number: "))
for item in range(1,11):
    print(item*multiple)  
               
multiple=int(input("enter a number: "))
for item in range(1,11):
    #print(multiple,"*",item,"=",item*multiple)       
    print(f"{multiple}*{item}={item*multiple}")
"""
"""
value=1 
iterations=int(input("enter the number of iteration: "))
while value<=iterations:
    print(value)
    value+=2  
    
""" 

for i in range(1,6):
    if i==3:
        break
    print(i)    

for i in range(1,6):
    if i==3:
        continue
    print(i)        
    
for i in range(1,6):
    if i==3:
        pass
    print(i)            