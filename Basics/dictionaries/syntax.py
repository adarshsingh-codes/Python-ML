student={
    "name":"Adarsh",
    "age": 20,
    "cgpa":9.3,
}

print(student["name"])  #prints onyl the value forr this

student["height"]=180
  
print(student)   #prints the full dictionary

student["age"]=65
print(student["age"])

del student["age"]

print(student)


#tocheck if a key exist
print("name" in student)

print("weight" in student)

for key in student:
    print(key)


for value in student.values():
    print(value)



#together it is called items(the key and values)
for key,value in student.items():
    print(key,value)



#these below work the same 
#normally
print(student["cgpa"])

#safer
print(student.get("cgpa"))
print(student.get("city"))


student2={
    "name":"Adarsh",
    "branch":"CSE",
}

student2["year"]=2

student2["branch"]="AI"


student2["department"]=student2["branch"]
del student2["branch"]
print(student2)
for key in student2:
    print(key)



for key,value in student2.items():
    print(key,"->",value)