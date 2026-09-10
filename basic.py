"""
print("wellcom python")

#getting user inputs
student_name=input("Enter your name: ")
student_age=int(input("Enter your age: "))
student_mark=float(input("Enter your mark: "))
is_present=bool(input("is present or not(T/F): "))
languages_known=input("Enter the language known: ").split(",")

#printing the data
print("The student name is: ",student_name)
print("The student age is: ",student_age)
print("The student mark is: ",student_mark)
print("Present or not: ",is_present)
print("Languages known: ",languages_known)

#type function
print(type(student_name))
print(type(student_age))
print(type(student_mark))
print(type(is_present))
print(type(languages_known))

#id()-built in function that retern unique identity of an object during its time
num1=10
num2=10
num3=20
print(id(num1))
print(id(num2))
print(id(num3))

list1=[1,2,3]
list2=[1,2,3]
print(id(list1))
print(id(list2))


valu1=25.56
valu2="hi"
print(isinstance(valu1,float))
print(isinstance(valu2,float))
print(isinstance(valu2,(int,float))) #topple

#implicit type conversion
data1=10
data2=20.5
data3=data1+data2
print(data3)

data4="30"
data5="45"
result=data4+data5
print(result)
"""


