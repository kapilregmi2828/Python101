# recursive function to find the factorial of x
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

x = int(input("Enter number to find factorial of: "))
print(factorial(x))