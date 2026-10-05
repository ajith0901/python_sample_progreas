#comprehension: it provided a concise and readable way to creat collection.
#list comprehension generate list,
#set comprehension generate set,
#dictionary comprehension generate dictionary,
#syntex:-expresion for item in iterable if condion

#list comprehension

number=[1,3,5,2,7]
odd_number=[item for item in number if item%2!=0]
print(odd_number)