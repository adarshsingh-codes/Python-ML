name="adarsh"
print(name)
print(type(name))
print(name[3])
print(name[-3])
print(name[0:4])
print(name[::-1]) #this reverses the thing


print(name[0:6:2])  #skip some parts

for ch in name:
    print(ch,end="")
print("\n")
for ch in range(len(name)):
    print(name[ch])


a="adarsh "
b="singh"

print(a+b)

print("ho"*3)

s="python"

print("P" in s)
print("z" in s)
print("t" in s)

print(len(s))

print(s.lower())

print(s.upper())

print(s.capitalize())


str="helLo i am adarsh"
print(str.casefold())

print(str.title())

print(str.swapcase())

str2="         jd        sd               "
print(str2)
print(str2.strip())

print(str2.lstrip()) #left spaces removed
print(str2.rstrip()) #right spaces removed

print(str.replace("adarsh","singh"))

print(str.find("m"))

print(str.index("m"))  #similar to find

print(str.count("a"))

print(s.startswith("he"))

print(str.startswith("he"))

print(str.endswith("hello"))

print(str.split())

a="asd ,asdf,asd,asdf"
print(a.split(","))

words=["i","love","mangoes"]

print(" ".join(words))

print("asdfa".isalpha())
print("1234".isdigit())
print("234rtgv!@#s".isalnum())

print("sdfgD".islower())
print("SDFGH".isupper())

print("25".zfill(5))

print("25".zfill(15))

text = "banana"

print(text.rfind("a"))#fidn fromright side
 

print(text.replace("a","x",2))