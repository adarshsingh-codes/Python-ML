s=input("Enter the string: ")
words=s.split(" ")
result=words[0]
for i in range(len(words)):
    if(i==0):
        continue
    result+=words[i].capitalize()
print(result)

# s = input("Enter the string: ")

# result = ""
# flag = False

# for ch in s:
#     if ch == ' ':
#         flag = True
#     elif flag:
#         result += ch.upper()
#         flag = False
#     else:
#         result += ch

# print(result)