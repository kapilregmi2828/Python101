# this is a recursive function to find a factorial of number x

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

x = int(input("Enter a number to find its factorial: "))

print(factorial(x))