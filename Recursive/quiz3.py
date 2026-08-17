# recursive function to find nth fibonacci 
# the counting start from nth index that is 0, [0,1,2,3,4,5 ...............]
 def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

x = int(input("Enter number to find fibonacci: "))
print(fibonacci(x))