# tuples are ordered, indexed, unchangeble, and allows duplicates.
# Since they are unchangeble it is used to store static info like username, password, login infos etc.
thistuple = ("apple", "banana", "orange")
print(thistuple)

print(len(thistuple))

if "banana" in thistuple:
    print("banana is in the tuple thistuple.")

# Updating the tuples. 

l1 = ("honda", "toyota", "nissan")
l2 = ("ford",)

l1 += l2 # we can add two tuples.
print(l1)

#adding an element on the tuple 

a1 = ("car", "bike", "ship")
a2 = list(a1)

a2.append("train")

a1 = tuple(a2)

print(a1)

x = ("red", "blue", "pink", "yellow")
print(x)
y = list(x)
y.remove("red")

x = tuple(y)

print(x)

b = ("accord", "camry", "versa")
print(b)

del b 

#print (b)

