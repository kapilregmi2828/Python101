# we can copy a list using copy() method, list() method, and (slice) : operator

list1 = ["apple", "banana", "mango"]
list2 = list1.copy()

print(list1)
print(list2)

list2 = list(list1)
print(list2)

list2 = list1[:]
print(list2)