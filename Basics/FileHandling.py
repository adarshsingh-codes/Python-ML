with open("data.txt","r") as file:   #here the "r" means we are reading from the file
    data=file.read()
print(data)

#writing to a file

with open("data.txt","w") as file:
    file.write("Hello python")


#adding without deleting existing content
with open("data.txt","a") as file:
    file.write("\nNew Line")


#remember
#"r"- read
#"w"- write/overwrite
#"a"- append

