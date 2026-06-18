s=input("Enter the string: ")
words=s.split(" ")
count=0
maxcount=len(words[0])
for word in words:
    count=len(word)
    if count>maxcount:
        maxcount=count
print(maxcount)
