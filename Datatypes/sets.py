set1 = {"apple", "banana", "cherry"}

for x in set1:
    print(x)

thislist = [1, 2, 3, 5, 8, "Ram", 1, 3, 3, "Kapil", "Ram", 3j]
print(thislist)

# remove duplicate items from thislist 

y = set(thislist)
print(y)

z = list(y)

print(z) # here we converted our list into set to remove duplicate items and converted back to list and printed. 
 
