"""
class CustomException(Exception):
    pass
def check_number(num):
    if num<0:
        raise CustomException("Not allow negative numbers") 
    return num
try:
    result=check_number(-7)
except CustomException as e:
    print(e)     
else:
    print(result)


class NameTooShortError(Exception):
    pass 
name=input("Enter the user name: ")
try:
    if len(name)<8:
        raise NameTooShortError("Name must be greater then 8 letter")
except NameTooShortError as e:
    print(e)
else:
    print(name)  
"""

class InsufficientBalanceError(Exception):
    pass
amount=int(input("Enter the amount: "))
balance=5000
try:
    if amount>balance:
        raise InsufficientBalanceError("amount is grater then available balance")
except InsufficientBalanceError as e:
    print(e)
else:
    remaining_balence=(balance-amount)
    print(remaining_balence)               




      
