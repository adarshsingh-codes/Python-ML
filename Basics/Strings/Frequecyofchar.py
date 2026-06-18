s=(input("Enter the string: "))
arr=[0]*26
for i in range(len(s)):
    ch=s[i]
    arr[ord(ch)-97]+=1
for i in range(len(arr)):
    if(arr[i]>=1):
        print(chr(i+ord('a')),":", arr[i])