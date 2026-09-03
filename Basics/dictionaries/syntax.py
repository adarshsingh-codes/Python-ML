student={
    "name":"Adarsh Singh",
    "marks":85
}

print(student["name"])
print(student["marks"])

student["marks"]=92
student["grade"]="A"

print(student)
if "grade" in student:
    print(student["grade"])