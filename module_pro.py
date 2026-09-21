"""
import math 

print(math.pi)
print(math.sqrt(49))
print(math.pow(2,3))


from math import sqrt

print(sqrt(5))
"""
"""
import random
import string

print(random.randint(150,200))
random_letter=random.choice(string.ascii_letters)
print(random_letter)

small_letter=random.choice(string.ascii_lowercase)
print(small_letter)

capital_letter=random.choice(string.ascii_uppercase)
print(capital_letter)

numbers=[2,3,5,6,7]
print(random.choice(numbers))
print(random.sample(numbers,k=2))
"""

#try out secret module
import secrets
import string

characters=string.ascii_letters+string.digits

secret_code="".join(secrets.choice(characters) for _ in range(6))
print("your secret number is: ",secret_code)

otp=secrets.randbelow(1000+9999)
print("ypur otp is: ",otp)
"""
import datetime

print(datetime.datetime.now())
print(datetime.date.today())
print(datetime.date.today()-datetime.timedelta(1))

from  datetime import datetime
now=datetime.now()
curenttime=now.time()
print(curenttime)

#try out betwen random days


import sys 

print(sys.platform)
print(sys.version)

import os 
print(os.getcwd())
print(os.listdir())

import datetime as dt 
print(dt.datetime.now())

import requests
url=requests.get('https://jsonplaceholder.typicode.com/users/1')
print(url.json())
"""
