n=int(input("Enter the size of the tuple: "))
arr=list(map(int,input().split()))
t=tuple(arr)
maxi=t[0]
sec_max = float('-inf')
for i in range(len(t)):
    if t[i]>maxi:
        sec_max=maxi
        maxi=t[i]
    elif maxi!=t[i] and sec_max<t[i]:
        sec_max=t[i]
if sec_max==float('-inf'):
    print("No second max")
else:
    print("The second largest element is: ",sec_max)