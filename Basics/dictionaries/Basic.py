student={
    "name": "Adarsh",
    "branch":"CSE",
    "year":2,
    "cgpa":8.4,
}
student["branch"]="AI"
student["city"]="Chennai"
student["gpa"]=student["cgpa"]
del student["cgpa"]
del student["year"]

print(student)

for key,value in student.items():
    print(key,value)
