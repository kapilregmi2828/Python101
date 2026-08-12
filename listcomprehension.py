fruits = ["apple", "banana", "kiwis", "cherry", "Mango"]
print(fruits)
newfruits = []

for x in fruits:
    if "a" in x:
        newfruits.append(x)

print(newfruits)

newlist = [x for x in fruits if "a" in x] # short line of code using for and in 
print(newlist)

list1 = [x for x in fruits]
print(list1)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in fruits]
print(newlist)

newlist = [x.lower() for x in fruits]
print(newlist)

newlist = ["hello" for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
