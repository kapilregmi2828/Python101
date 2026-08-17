# Rescursion is when a function call itself. 
# this is a simple recursive function that counts down to number (x).

def countdown(n):
    if n <=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1)

x = int(input("Enter a number to start countdown! :"))
countdown(x)

