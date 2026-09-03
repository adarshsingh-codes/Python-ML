
#this code means  

try:             #try this code
    x = int(input("Enter number: "))
    print(10 / x)

except ValueError: #and if this particular error happens , EXCEPT do this instead
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")




#we cna also add else to it so that it will run if thwre is no exception currently 


#finally runs 
#regardless of whether an error happened
finally:
    print("Program finished")



#some errors include:

#ValueError - wrong value input

#TypeError - when we try to combine different datatype eg: string+int

#IndexError - if an index doesnt exist and we call it 

#KeyError - if in a  dictionaru a ley doesnt exist and we call it

#NameError -if a varibales= doest exist nd we call it


#FileNotFoundError - whena  file doesnt exist like file=open("data.txt") and it isnt there

#AttributeError - Object doesn't have that attribute/method

#ZeroDivisionError -Division by zero