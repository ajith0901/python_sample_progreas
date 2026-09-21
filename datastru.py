#string-immutable data structor
#list-[]orderd collection, mutable,allow duplicates,can be accesed using indexing
#tupple- ()orderd collection, mutable,allow duplicates,can be accesed using indexing
#set- {}unorder collection,mutable,doesnot allow duplicates,cnnot be accesed using index
#dictionar-{key:valu} ordered collection,valu can be changed,allow duplicate values,can be accessed

username="ajith"

"""
0  1  2  3  4  #positive indexing
-5 -4 -3 -2 -1
a  j   i  t  h
1  2  3  4  5  #lenth

print(username[2])
print(len(username))
print(username[-2])
"""

#string slicing
#[start:stop:step]
#start-start defalt value is 0
#stop-valu-1
#step-number of skip (defaultly 1 for positive numbers)
"""
data="python is a programing language"
print(data[:9])

data="python is a programing language"
print(data[2:9])
print(data[2:12:3])
print(data[6:])
print(data[1:10:-2]) #it will not work
print(data[-1])
print(data[10:1:-1])
print(data[10:2])
print(data[-10:-2])
print(data[::-2])

#string methods
text="python is the dynomic language"
print(text.upper()) #all letter are capitel
print(text.lower()) #all letter are small letter
print(text.capitalize()) #starting letter only capitel
print(text.title()) #every word firts letter capitel letter
print(text.startswith("yt"))
print(text.endswith("good"))
#text[0]="r"
print(text)
print(id(text))
uppercase=text.upper()
print(id(uppercase))
"""

#list
#crud operation
#list creation
#list viewing
#list updating
#list deleting
"""
userdata=["ajith",24,"marthandam",]
print(userdata)
userdata.insert(1,"maria")
print(userdata)
userdata.append(2020)
userdata.extend("python")
userdata.append(["english","hindi","malayalam"])
print(userdata)
print(userdata[11])
print(userdata[11][0])
userdata.extend(["html","css"])
print(userdata)
userdata[1]="AJITH"
print(userdata)
userdata.remove("marthandam")
print(userdata)
#userdata.remove("mtm")
#print(userdata)
userdata.pop(2)
userdata.reverse()
print(userdata)


#tuple
tuple1=(1,2,3,4)
print(tuple1)

#nested tuple
tuple2=("ajith","aji","kumar",(6,7,8))
print(tuple2)

#tuple unpacking
person=("ajith",23,"mtm")
name,age,place=person
print(name)
print(place)
print(age)

num=(10,20,30,40,50)
a,b,*c=num
print(c)
print(a)

num=(10,20,30,40,50)
e,*f,g=num
print(e)
print(f)
print(g)

num2=(10,20,20,30,40,40,50)
print(num2.count(20))
print(num2.index(30))
print(num[2])

name=input("enter a string: ")
count=0
for char in name:
    count+=1
print("the count is: ",count)  
""" 
"""
user_input=input("enter a word: ")
for letter in user_input:
    if user_input.count(letter)==1:
        print("first non repearing charector is: ",letter)
        break
else:
    print("no non-repeating charector") 

#repeating charector index,second non repeating 
"""
"""
#set-{
student1={"english","hindi","malayalam"}
student2={"english","hindi","python"}
student3={"english","urudhu"}
student1.add("c")
print(student1)
#student1.add("kannada","marathi") #only one arguments just like append
student1.update(["c++","java"])
print(student1)
student1.pop()
print(student1)
#student1.remove("hindi")
#print(student1)


#union interstion diference symntric differens
print(student1)
print(student2)
print(student1.union(student2))
print(student1|student2)

#intersection
print(student1)
print(student2)
print(student1.intersection(student2))
print(student1&student2)

#difference
print(student1)
print(student2)
print(student1.difference(student2))
print(student1-student2)

#symmetric difference
print(student1)
print(student2)
print(student1.symmetric_difference(student2))

#subset is superset is disjoint

#frozenset = immutable
fs1=frozenset("ajith")
fs2=frozenset([1,2,3,4,2,3,4])
print(fs1)
print(fs2)

#dictionary
student={
    "name":"Ajith",
    "age":24,
    "place":"mtm"
}
print(student)
print(student["name"])

info=dict(city="mtm",state="tn")
print(info)

print(info.keys())
print(info.values())

#print(info["city"])

student.pop("age")
print(student)

for key,value in student.items():
    if key=="name":
        print(key,value)

employee={
    "emp1":{
        "name":"aji",
        "age":24,    
    },
    "emp2":{
        "name":"ajith",
        "age":23,
    },
    "emp3":{
        "name":"kumar",
        "age":22,
    },
}    
print(employee["emp1"]["age"])
print(employee["emp2"])
print(employee)

"""