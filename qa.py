"""
user_input=input("enter a word: ")
count=0
for letter in user_input:
    if user_input.count(letter)==1:
        count+=1
        if count==2:
            print("secound non repeatring charector is: ",letter)
            break
else:
    print("no non-repeating charector") 

"""  
 

user_input=input("enter a word: ")
for i in range(len(user_input)):
    repeat=False
    for j in range(len(user_input)):
        if i==j:
            repeat=True
            print("secound non repeatring charector is: ",user_input)
            break
else:
    print("no non-repeating charector") 




