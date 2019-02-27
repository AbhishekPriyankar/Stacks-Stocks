dict = dict()

dict["Name"] = "Abhishek"
dict["Height"] = 173
dict["Age"] = 23

print(dict)

print(dict.keys())
print(dict.values())

for x,y in enumerate(dict):
    print(x , y, dict[y])

for i in dict:
    print(i , dict[i])


