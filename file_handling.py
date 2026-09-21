"""
store_data=open("newfile.text","w") #FILE AUTOMETICALY CREATED WHEN GIVEN W
store_data.write("welcom to python program")
print(store_data)
store_data.close()

read_data=open("new_file.txt","r")
print(read_data.read())
read_data.close()

append_data=open("new_file.txt","a")
append_data.write("\npython is an interprited language")
print(append_data)
append_data.close()

read_data=open("new_file.txt","r")
print(read_data.read())
read_data.close()

#using context manager

with open("new_file.txt","r") as f:
    print("current position: ",f.tell())
    f.read(6)
    print("after read position is: ",f.tell())
    f.seek(4)
    print("after seek: ",f.tell())
    print(f.read())

with open("car image.jpg","rb") as data: #read bits
    print(data.read()) 

data=open("delete_file.txt","x") #exclusive creation       
print(data)
data.close()
"""
"""
file_path="delete_file.txt"
import os 
if os.path.exists(file_path):
    os.remove(file_path)
    print(f"{file_path} deleted successfully")
else:
    print("file not exists")   
"""
#serialization
import pickle 
data={
    "students":["aji","ajith","kumar"]
}    

#serialization saving data to file 
with open("user_details.pkl","wb") as f:
    pickle.dump(data,f)
    print("data is serialized to user details")  

#deserialization retriving data
with open("user_details.pkl","rb") as f:
    pickle.load(f)
    print("data is serialized to user details")
   
#seralization saving data into memory

dump_data=pickle.dumps(data)
print("data is serializaed to bytes: ",dump_data)

load_data=pickle.loads(dump_data)
print("deserialized data to bytes: ",load_data)


import json 
data={
    "students":["aji","ajith","kumar"]
}    

#serialization saving data to file 
with open("user_details.json","w") as f:
    json.dump(data,f)
    print("data is serialized to user details")

#deserialization retriving data
with open("user_details.json","r") as f:
    load_data=json.load(f)
    print("data is serialized to user details: ",load_data)

#seralization saving data into memory

dump_data=json.dumps(data)
print("data is serializaed to bytes: ",dump_data)

load_data=json.loads(dump_data)
print("deserialized data to bytes: ",load_data)  

   