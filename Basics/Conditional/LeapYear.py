year=int(input("Enter the year: "))
if year%400==0 or (year%4==0 and year%100!=0):
    print(year,"is a leap year")
else:
    print(year,"is not a leap year")




#Empty strings, empty lists, 
# empty dictionaries, 0, None, 
# etc. generally evaluate to False
#This becomes useful everywhere in Python, 
# including ML/data-processing code