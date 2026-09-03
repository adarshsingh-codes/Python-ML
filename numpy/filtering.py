import numpy as np

#Filtering= Refers to the process of selecting elements from an
#           array that match a given condition 

array=np.array([10,20,30,40,50])

filtered=array[array>25]

print(filtered)


ages=np.array([[21,17,19,20,16,30,18,65],
               [39,22,15,99,18,19,20,21]])

teenagers=ages[ages<18]
print(teenagers)

adults=ages[(ages>=18) & (ages<65)]
print(adults)

seniors=ages[ages>=65]
print(seniors)

evens=ages[ages%2==0]
print(evens)




#this is a slow version fo the above method so meh
adults1=np.where(ages>=18,ages,0)   #this returns the original shape
#condition,array,fill vlaue
print(adults1)