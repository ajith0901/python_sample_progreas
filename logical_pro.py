"""
numberlist=[]
num_of_element=int(input("enter the number: "))  #range value
for element in range(num_of_element):
    num=int(input(f"enter the element {element+1}: "))
    numberlist.append(num)

largest_num=numberlist[0]
smallest_num=numberlist[0]
for num in numberlist:
    if num>largest_num:
        largest_num=num
    if num<smallest_num:
        smallest_num=num
print("largest number in the list is:",largest_num)
print("smallest number in the list is:",smallest_num)   
"""

#13 5 6 7 8
#largest number is 13
#smallest number is 13
#num=13
#first itration num>largest - false, num<mallest -false
#second iteration num-5, largest=13,smallest=13 true smallest =5
#third iteration num=6 largest =13 smalest=5  false
#fourth iteration num=7, largest=13 smalest=5  false

#seperate list of elements as positive and negetine number list
"""
numberlist=[]
positive_list=[]
negative_list=[]
num_of_element=int(input("enter the number: "))  #range value
for element in range(num_of_element):
    num=int(input(f"enter the element {element+1}: "))
    numberlist.append(num)

for num in numberlist:
    if num>=0:
        positive_list.append(num)
    if num<=0:
        negative_list.append(num)
print("positive number in the list is:",positive_list)
print("negative number in the list is:",negative_list) 

#number of occurence of given number in a tuple

count=0
number=tuple(map(int,input("enter the number to be inserted").split()))
number_to_check=int(input("enter the number to count"))
for element in number:
    if element==number_to_check:
        count+=1
print(f"occurence of number {number_to_check} in tuple is {count}")  

#revers the dictionary

data={"a":1,"b":2,"c":3}
revers_data={}
reversed_keys=list(data.keys())   #["a","b","c"]
for key in reversed_keys[::-1]:
    revers_data[key]=data[key]
print("reversed data:",revers_data)    

#linear search

user_marks=list(map(int,input("enter the number to be inserted: ").split()))
search_element=int(input("enter the element to search: "))
for i in range(len(user_marks)):
    if search_element==user_marks[i]:
        print(f"element fount at index {i}")
        break
else:
    print("element not fount")
 

#fibonacci serie
#0 1 1 2 3 5 8
#a=0,b=1,c=0+1=1,
#a=b,b=c
#a=1,b=1,c=1+1=2
#a=1,b=2,c=1+2=3
#a=2,b=3,c=2+3=5
#a=3,b=5,=c=3+5=8
a=0
b=1
number_of_iteration=int(input("enter the number of iteration: "))
for element in range(number_of_iteration):
    print(a)
    c=a+b
    a=b
    b=c    

#prime number 
#mor then two degit numbers sqreroot by the number
num=int(input("enter the number:"))
for i in range(2,num):
    if num % i==0:
        print("not prime number")
        break
else:
    print("its prime numer")    

#palindrome

#bubble sorting making a element in asending order
#13 89 75 10 51
#13>89 -false 
#13>75 -false
#13>10 -swap 13 gratrt then 10 so swap the iteration
#10 89 75 13 51
#89>75  swap
#10 75 89 13 51
#75>89
#75>13 swap
#10 13 89 75 51
#89>75 swap
#10 13 75 89 51
#75>89
#75>51 swap
#10 13 51 89 75
#89>75 swap
#10 13 51 75 81

def bubblesort(num):
    n=len(num)
    for i in range(n):
        for j in range(i+1,n):
            if num[i]>num[j]:
                temp=num[i]
                num[i]=num[j]
                num[j]=temp
    return num
print(bubblesort([13,89,75,10,51]))

#pattern
number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,number+1):
        print("*",end="")
    print()    

number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,number+1):
        print(col,end="")
    print()     

number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,number+1):
        print(row,end="")
    print()            

number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print("*",end="")
    print()   

#left side row
number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print(row,end="")
    print()       

#left side col
number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        print(col,end="")
    print()     

number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,row+1):
        if row>=col:
            print("*",end=" ")
    print()   

number=int(input("enter the number of element:"))
for row in range(1,number+1):
    for col in range(1,col+1):
        if row<=col:
            print("*",end="")
    print()         

    123456789
"""

number=int(input("enter the number of element:"))
num=1
for row in range(1,number+1):
    for col in range(1,row+1):
            print(num,end="")
            num+=1
    print()         

number=int(input("enter the number of element:"))
num=1
for row in range(1,number+1):
    my_list=[]
    for col in range(1,row+1):
        my_list.append(str(num))

        num+=1
    print("".join(my_list[::-1])) 

number=int(input("enter the number of element:"))
num=1
for row in range(1,number+1):
    my_list=[]
    for col in range(1,col+1):
        my_list.append(str(num))

        num+=1
    print("".join(my_list[::-1]))                 
                

