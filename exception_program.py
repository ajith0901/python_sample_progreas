#unexpected events are called exception that we can resolve or handle
#eg: forgot password etc..(exception handling-resolveing problems)
#keyword"1:try what are the types of problem that gonna to form work as a pair
#2.except-problem solver(try+except=problem resolve)
#3.finally-normaly used for the closing the connection with the database
#In builled class they provided by python
"""
print("statement 1")
print("statement 2")
print("statement 3")
try:
    value1=10
    value2=0
    value3=value1/value2 #zero division error
except ZeroDivisionError:
    print("denominator cant be zero")   
print("statement 4")
print("statement 5")


#TRY expect else
numerator=int(input("enter the number"))
denominator=int(input("enter the denominator"))
try:
    quotient=numerator/denominator
except ZeroDivisionError:
    print("denominator cant be zero") 
else:
    print(quotient)  

#type error  
try:
    num1=15
    num2="25"      
    add=num1+num2
    print(add)
except TypeError:
    print("string cant be added with integer value") 

#index error-index out of range
numbers=[1,2,3,4,5,6,7]
try:
    print(numbers[10])
except IndexError:
    print("index out of range")        

#KEY ERROR-dictionary
book_details={
    "book_id":2,
    "book_name":"python"
}
try:
    print(book_details["book_author"])
except KeyError:
    print("key not found") 

#file not found error=serching for a non available file
try:
    with open("test_file.txt","r") as f:
        print(f,read())
except FileNotFoundError:
    print("file not found in directory")        

#import error-
try:
    from math  import square
except ImportError as e:
    print(e)    #what is the error formed on that class non showing the error


#attribute error
try:
    user_value="welcom"
    print(user_value.add())
except AttributeError as e:
    print(e) 

#value error-when no proper value is given
try:
    data=int("ajith")
except ValueError as e:
    print(e)  

#name error-print an not available variable
try:
    print(student)
except NameError as f:
    print(f)
finally:
    print("executed normally")   
"""
#multiple exception more then one exception (handile one exception at a time)
#resolve the first problem in multiple exception 
try:
    user_value="welcom"
    print(user_value.add())

    data=int("ajith")
except ValueError as e:
    print(e)  
except AttributeError as e:
    print(e)     

#multiple exception using another method
try:
    user_value="welcom"
    print(user_value.add())

    data=int("ajith")
except (ValueError,AttributeError) as e: 
    print(e)  