# we can loop through the list using for loop, while loop, range/len, and list comprehension

list1 = ["Apple", "Banana", "Mango"]

for i in list1: # loop list using for loop
    print(i)

for x in range(len(list1)): # using range and len
    print(list1[x])

a = 0
while a < len(list1): # using while loop
    print(list1[a])
    a +=1 

[print(x) for x in list1] # shortest list comprehension using for loop.