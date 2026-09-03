
# a dictionary stores key value pairs;

freq={}   #empty dictionary
my_set = set()  # empty set
arr=[]  #empty arr  #pyhotn calls it a list


student={
    "name": "Adarsh",
    "branch":"CSE",
    "year":3,
    "cgpa":9.3,
}

if "year" in student:
    print(student["year"])


print(student)   #prints the full dictionary
student["branch"]="AI"
student["city"]="Chennai"
student["gpa"]=student["cgpa"]
del student["cgpa"]
del student["year"]

for key,value in student.items():
    print(key,value)


#methods
print(student.keys())
student.values()
student.items()
print(student.get("name"))



#tocheck if a key exist
print("name" in student)

print("weight" in student)



#these below work the same 
#normally
print(student["cgpa"])

#safer
print(student.get("cgpa"))



#Why dictionaries matter for AI engineering

#You'll constantly encounter data like:

#user = {
 #   "name": "John",
#    "age": 25,
#    "embedding": [0.12, 0.45, 0.78],
 #   "metadata": {
  #      "source": "article",
 #       "category": "technology"
 #   }
#}

#APIs, JSON, LLM responses, RAG metadata, configuration files, etc. use this structure heavily.


#dictionary comprehension


squares={x: x*x for x in range(5)}