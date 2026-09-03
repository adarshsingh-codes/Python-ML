


#python strings are immutable
#once created they cnt be destroyed


text="Hello world"

print(text[0:5])
print(text[:5])    #first 5
print(text[0:])     #from index 0
print(text[6:])     #from index 6
print(text[:])      #entire string
print(text[::2])    #every second string
print(text[::-1])   #reverse


text1="      adarhs SINgh     "
print(text1.strip())
print(text1.lower())
print(text1.upper())

text1.replace("SINgh","Python")
print(text1)

text2="Python is powerful"
words=text2.split()

print(words)




#remember: 
#[start:stop:step]  for idnexing or slicing