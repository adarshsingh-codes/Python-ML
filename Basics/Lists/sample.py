numbers=[10,20,30,40,50]

print(numbers[2])

numbers[1]=25

numbers.append(60)

print(numbers[::-1])

greater_than_25=[x for x in numbers if x>25];
print(greater_than_25)