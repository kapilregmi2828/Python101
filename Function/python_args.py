def my_kids(*kids):
    print("My childrens are:",kids[0:2])

my_kids("Ram", "Shyam", "Gopal")

def my_sum(*numbers):
    total = 0
    for x in numbers:
        total += x 
    return total

print(my_sum(1, 5, 9))
print(my_sum(100))