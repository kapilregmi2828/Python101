# def fun1():
#     print("Hello this is Function fun1")

# fun1()

def add_function(a,b): # here a and b are parameters 
    return a+b

x = int(input("enter first number to add:"))
y = int(input("Enter second number to add:"))

result = add_function(x,y) # x and y are arguments
print("The sum is:",result)