# recursive function for a countdown generator

def count_down(n):
    if n <= 0:
        print("Done!")
    else: 
        print(n)
        return count_down(n-1)

x = int(input("Enter number to start countdown from: "))
count_down(x)