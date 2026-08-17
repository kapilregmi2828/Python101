# Python iterators is an object that lets you loop through the elements of a collection one item at a time.

mytuple = ("apple", "banana", "cherry")

myit = iter(mytuple) # loops through the tuple one item at a time
print(next(myit)) # prints the next item in the tuple. 
