s=input("Enter the string: ")
arr=[0]*26
for i in range(len(s)):
    arr[ord(s[i])-97]+=1
for i in range(len(s)):
    if arr[ord(s[i])-97]==1:
        print(s[i])
        break
    
