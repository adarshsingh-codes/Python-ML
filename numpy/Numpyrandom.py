import numpy as np

rng= np.random.default_rng() 
#this creates a random number

print(rng.integers(low=1,high=101))   

print(rng.integers(1,100,size=3))    #1D 

print(rng.integers(low=1,high=100,size=(3,2))) #2d array


#if we wanna produce the same result


rng1=np.random.default_rng(seed=1)  # for same to be repeated then just put seed=1
print(rng1.integers(low=1,high=101,size=(3,2)))




#floating point number

np.random.seed(seed=1)

print(np.random.uniform())  #randome number between 0 and 1

print(np.random.uniform(low=-1,high=1))

print(np.random.uniform(low=-1,high=1,size=(3,2)))




rng=np.random.default_rng()
array=np.array([1,2,3,4,5])
rng.shuffle(array) #shuffles a array

print(array)


fruits=np.array(["apple","banana","watermelon","orange"])
#rng.shuffle(fruits)
fruit=rng.choice(fruits)
fr=rng.choice(fruits,size=3)

fr=rng.choice(fruits,size=(3,3))
print(fruit)
